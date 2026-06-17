---
layout: archive
title: "Miscellaneous"
permalink: /miscellaneous/
author_profile: false
body_class: misc-gallery-page
redirect_from: 
  - /md/
  - /markdown.html
  - /markdown/
---

This page collects selected photographs from travel, daily life, and academic journeys.

<div class="photo-gallery">
{% assign photo_count = 0 %}
{% for file in site.static_files %}
  {% if file.path contains '/images/travel/' %}
    {% assign ext = file.extname | downcase %}
    {% if ext == '.jpg' or ext == '.jpeg' or ext == '.png' or ext == '.webp' %}
      {% assign photo_count = photo_count | plus: 1 %}
      <a href="{{ file.path | relative_url }}">
        <img src="{{ file.path | relative_url }}" alt="Travel photograph {{ photo_count }}">
      </a>
    {% endif %}
  {% endif %}
{% endfor %}
</div>

{% if photo_count == 0 %}
<p><em>Photographs will be added here as image files are uploaded to <code>images/travel/</code>.</em></p>
{% endif %}

<style>
.photo-gallery {
  column-count: 3;
  column-gap: 16px;
  margin-top: 24px;
}

.photo-gallery a {
  display: inline-block;
  width: 100%;
  margin: 0 0 16px;
}

.photo-gallery img {
  width: 100%;
  height: auto;
  border-radius: 3px;
  display: block;
}

.photo-gallery img:hover {
  opacity: 0.88;
}

@media (max-width: 900px) {
  .photo-gallery {
    column-count: 2;
  }
}

@media (max-width: 600px) {
  .photo-gallery {
    column-count: 1;
  }
}
</style>
