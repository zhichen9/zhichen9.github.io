---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<h1 style="font-weight:700; text-align:center; margin-bottom:25px;">🌍 Travel Gallery</h1>

<p style="font-size: 16.5px; color:#555; text-align:center; max-width:750px; margin:0 auto 40px;">
A collection of my travel memories over the years — capturing moments from different cities, cultures, and experiences across the world.
</p>

<!-- ===================
   🇮🇹 Italy
=================== -->
<section style="margin-bottom:60px;">
  <div class="travel-header" style="--accent-color:#c0392b;">
    <h2>🇮🇹 October 2022 – Italy Memories</h2>
    <p>Walking through Rome’s ancient ruins and Venice’s quiet canals — a timeless journey of history and beauty.</p>
  </div>

  <div class="gallery">
    {% for i in (1..12) %}
      <img src="{{ site.baseurl }}/images/travel/2022/oct_italy/2022_italy_{{ i }}.jpg" alt="Italy photo {{ i }}">
    {% endfor %}
  </div>
</section>


<!-- ===================
   🇫🇷 France
=================== -->
<section style="margin-bottom:60px;">
  <div class="travel-header" style="--accent-color:#e67e22;">
    <h2>🇫🇷 September 2022 – France Memories</h2>
    <p>From the Louvre to the Eiffel Tower — exploring art, architecture, and romance under the Parisian lights.</p>
  </div>

  <div class="gallery">
    {% for i in (1..28) %}
      <img src="{{ site.baseurl }}/images/travel/2022/sep_france/2022_france_{{ i }}.jpg" alt="France photo {{ i }}">
    {% endfor %}
  </div>
</section>


<!-- ===================
   🇩🇪 Germany
=================== -->
<section style="margin-bottom:60px;">
  <div class="travel-header" style="--accent-color:#007acc;">
    <h2>🇩🇪 August 2022 – Germany Memories</h2>
    <p>Exploring the historic streets of Berlin and the waterways of Hamburg — culture, history, and color combined.</p>
  </div>

  <div class="gallery">
    {% for i in (1..36) %}
      <img src="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg" alt="Germany photo {{ i }}">
    {% endfor %}
  </div>
</section>


<hr style="margin-top:40px; margin-bottom:10px;">
<p style="text-align:center;">
<b>Email:</b> <a href="mailto:zhichen.colin@gmail.com">zhichen.colin@gmail.com</a>
</p>


<!-- ===================
   💅 CSS Design
=================== -->
<style>
/* Section Header Styling */
.travel-header {
  background: #f8f9fa;
  border-left: 6px solid var(--accent-color);
  padding: 15px 20px;
  border-radius: 8px;
  margin-bottom: 25px;
}
.travel-header h2 {
  margin: 0;
  color: var(--accent-color);
  font-weight: 700;
  font-size: 22px;
}
.travel-header p {
  color: #555;
  margin-top: 6px;
  font-size: 15.5px;
}

/* Gallery Grid */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 12px;
  margin-bottom: 30px;
}

/* Uniform Image Style */
.gallery img {
  width: 100%;
  height: 230px;
  object-fit: cover; /* 保证不变形 */
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.gallery img:hover {
  transform: scale(1.04);
  box-shadow: 0 6px 15px rgba(0,0,0,0.25);
}
</style>


