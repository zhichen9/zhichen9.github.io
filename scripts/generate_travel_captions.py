#!/usr/bin/env python3
"""
Analyze travel photos with a vision LLM and update _data/travel/descriptions.yml.

Requirements:
  pip install openai pyyaml

Usage:
  set OPENAI_API_KEY=your-key
  python scripts/generate_travel_captions.py --section nov_denmark
  python scripts/generate_travel_captions.py --all
  python scripts/generate_travel_captions.py --all --dry-run

Each photo gets a unique caption based on visible content (time, place, weather,
people, architecture, scene). Output is written back to descriptions.yml.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Install dependencies: pip install openai pyyaml", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
TRAVEL_DIR = ROOT / "images" / "travel" / "2022"
YAML_PATH = ROOT / "_data" / "travel" / "descriptions.yml"

SECTION_COUNTRY = {
    "dec_finland": "Finland",
    "nov_denmark": "Denmark",
    "oct_italy": "Italy",
    "sep_france": "France",
    "aug_germany": "Germany",
}

PROMPT = """You are writing captions for an academic personal travel gallery.
Analyze THIS photo only. Describe what is actually visible.

Return valid JSON with exactly these keys:
{
  "title_en": "Short English title with place name",
  "title_zh": "中文标题",
  "date": "Best estimate, e.g. Nov 8, 2022 or Dec 2022",
  "location_en": "City, Country (infer from architecture/signs if needed)",
  "location_zh": "中文地点",
  "weather_en": "Visible weather/light, e.g. Overcast, cold, 4°C",
  "weather_zh": "中文天气",
  "landmark_en": "Main building, scene, or subject",
  "landmark_zh": "中文地标/场景",
  "description_en": "2-3 unique sentences: time, location, weather, people, architecture, mood. Do NOT use generic templates.",
  "description_zh": "2-3 unique Chinese sentences matching the same facts."
}

Trip context: European travel in Aug–Dec 2022. Album folder hint: {section} ({country_hint}).
If the image clearly shows a different city/country, use the correct location — do not force the folder name.
Be factual. If unsure of exact landmark, describe the scene precisely."""


def encode_image(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def discover_photos(section: str) -> list[tuple[int, Path]]:
    folder = TRAVEL_DIR / section
    if not folder.is_dir():
        raise FileNotFoundError(f"Missing folder: {folder}")
    country = SECTION_COUNTRY.get(section, section)
    pattern = re.compile(rf"^2022_{re.escape(country.lower())}_(\d+)\.jpg$", re.I)
    items: list[tuple[int, Path]] = []
    for path in sorted(folder.glob("*.jpg")):
        match = pattern.match(path.name)
        if match:
            items.append((int(match.group(1)), path))
    return sorted(items, key=lambda x: x[0])


def analyze_photo(client: OpenAI, model: str, section: str, photo_id: int, path: Path) -> dict:
    country_hint = SECTION_COUNTRY.get(section, section)
    prompt = PROMPT.format(section=section, country_hint=country_hint)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encode_image(path)}",
                            "detail": "high",
                        },
                    },
                ],
            }
        ],
        response_format={"type": "json_object"},
        max_tokens=800,
    )
    raw = response.choices[0].message.content or "{}"
    data = json.loads(raw)
    data["id"] = photo_id
    required = [
        "title_en", "title_zh", "date", "location_en", "location_zh",
        "weather_en", "weather_zh", "landmark_en", "landmark_zh",
        "description_en", "description_zh",
    ]
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(f"Missing keys for {path.name}: {missing}")
    return data


def dump_section_entries(section: str, entries: list[dict]) -> str:
    lines = [f"{section}:"]
    for entry in entries:
        lines.append("  - id: {}".format(entry["id"]))
        for key in [
            "title_en", "title_zh", "date", "location_en", "location_zh",
            "weather_en", "weather_zh", "landmark_en", "landmark_zh",
            "description_en", "description_zh",
        ]:
            value = entry[key]
            if "\n" in value:
                value = value.replace("\n", " ")
            escaped = value.replace('"', '\\"')
            lines.append(f'    {key}: "{escaped}"')
    return "\n".join(lines) + "\n"


def replace_section_block(section: str, entries: list[dict]) -> None:
    text = YAML_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"^{re.escape(section)}:\n(?:  - id:.*?(?:\n    .*?)*\n)+",
        re.MULTILINE | re.DOTALL,
    )
    replacement = dump_section_entries(section, entries)
    if not pattern.search(text):
        raise ValueError(f"Section block not found in YAML: {section}")
    YAML_PATH.write_text(pattern.sub(replacement, text, count=1), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate unique travel photo captions with vision LLM")
    parser.add_argument("--section", help="Album key, e.g. nov_denmark")
    parser.add_argument("--all", action="store_true", help="Process all known sections")
    parser.add_argument("--model", default=os.getenv("OPENAI_VISION_MODEL", "gpt-4o-mini"))
    parser.add_argument("--dry-run", action="store_true", help="Print results without writing YAML")
    args = parser.parse_args()

    if not args.all and not args.section:
        parser.error("Provide --section NAME or --all")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)

    sections = list(SECTION_COUNTRY.keys()) if args.all else [args.section]
    client = OpenAI(api_key=api_key)

    for section in sections:
        photos = discover_photos(section)
        if not photos:
            print(f"No photos found for {section}", file=sys.stderr)
            continue
        print(f"Analyzing {len(photos)} photos in {section}...")
        entries = []
        for photo_id, path in photos:
            print(f"  [{photo_id}] {path.name}")
            entry = analyze_photo(client, args.model, section, photo_id, path)
            entries.append(entry)

        if args.dry_run:
            print(dump_section_entries(section, entries))
            continue

        replace_section_block(section, entries)
        print(f"Updated section {section} in {YAML_PATH}")


if __name__ == "__main__":
    main()
