---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<h1 style="font-weight:700; text-align:center; margin-bottom:15px;">🌍 Travel Gallery</h1>

<p style="font-size:16.5px; color:#555; text-align:center; max-width:750px; margin:0 auto 25px;">
A curated collection of my travel memories — moments and stories from different cities and countries around the world.
</p>

<!-- ===================
 🔗 Navigation Menu
=================== -->
<nav class="travel-nav">
  <a href="#italy">🇮🇹 Italy</a>
  <a href="#france">🇫🇷 France</a>
  <a href="#germany">🇩🇪 Germany</a>
</nav>

<hr style="margin-top:10px; margin-bottom:35px;">


<!-- ===================
 🇮🇹 Oct 2022 – Italy Memories
=================== -->
<section id="italy" class="travel-block" style="--accent-color:#c0392b; --bg1:#fff5f2; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇮🇹 Oct 2022 – Italy Memories</h2>
    <p>Wandering through Rome’s ancient ruins and Venice’s serene canals — a journey through time and beauty.</p>
  </div>

  <div class="gallery">
    {% for i in (1..12) %}
      <img src="{{ site.baseurl }}/images/travel/2022/oct_italy/2022_italy_{{ i }}.jpg" alt="Italy photo {{ i }}">
    {% endfor %}
  </div>

  <div class="back-top"><a href="#top">⬆ Back to Top</a></div>
</section>


<!-- ===================
 🇫🇷 France
=================== -->
<section id="france" class="travel-block" style="--accent-color:#e67e22; --bg1:#fff9f0; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇫🇷 Sep 2022 – France Memories</h2>
    <p>From the Louvre to the Eiffel Tower — art, architecture, and the rhythm of Paris nights.</p>
  </div>

  <div class="gallery">
    {% for i in (1..28) %}
      <img src="{{ site.baseurl }}/images/travel/2022/sep_france/2022_france_{{ i }}.jpg" alt="France photo {{ i }}">
    {% endfor %}
  </div>

  <div class="back-top"><a href="#top">⬆ Back to Top</a></div>
</section>


<!-- ===================
 🇩🇪 Germany
=================== -->
<section id="germany" class="travel-block" style="--accent-color:#007acc; --bg1:#f0f8ff; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇩🇪 Aug 2022 – Germany Memories</h2>
    <p>Exploring Berlin’s vibrant streets and Hamburg’s peaceful waterways — where history meets modern charm.</p>
  </div>

  <div class="gallery">
    {% for i in (1..36) %}
      <img src="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg" alt="Germany photo {{ i }}">
    {% endfor %}
  </div>

  <div class="back-top"><a href="#top">⬆ Back to Top</a></div>
</section>


<hr style="margin-top:40px; margin-bottom:10px;">
<p style="text-align:center;">
<b>Email:</b> <a href="mailto:zhichen.colin@gmail.com">zhichen.colin@gmail.com</a>
</p>

<style>
/* ========= Navigation Bar ========= */
.travel-nav {
  text-align: center;
  margin-bottom: 10px;
}
.travel-nav a {
  display: inline-block;
  color: #333;
  background: #f0f3f6;
  padding: 8px 16px;
  margin: 5px;
  border-radius: 25px;
  font-weight: 600;
  font-size: 15px;
  text-decoration: none;
  transition: background 0.3s ease, color 0.3s ease;
}
.travel-nav a:hover {
  background: #007acc;
  color: white;
}

/* ========= Section Container ========= */
.travel-block {
  background: linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%);
  padding: 35px 25px 40px 25px;
  border-radius: 14px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  margin-bottom: 65px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.travel-block:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

/* ========= Section Header ========= */
.travel-header {
  border-left: 6px solid var(--accent-color);
  padding-left: 15px;
  margin-bottom: 18px;
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

/* ========= Masonry Layout ========= */
.gallery {
  column-count: 3;
  column-gap: 12px;
  margin-top: 10px;
}

.gallery img {
  width: 100%;
  height: auto;
  margin-bottom: 12px;
  border-radius: 8px;
  break-inside: avoid;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery img:hover {
  transform: scale(1.03);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* ========= Back to Top ========= */
.back-top {
  text-align: right;
  margin-top: 10px;
}
.back-top a {
  font-size: 14px;
  color: #007acc;
  text-decoration: none;
}
.back-top a:hover {
  text-decoration: underline;
}

/* ========= Responsive ========= */
@media (max-width: 1000px) {
  .gallery { column-count: 2; }
}
@media (max-width: 700px) {
  .gallery { column-count: 1; }
}
</style>
