---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<h1 id="top" style="font-weight:700; text-align:center; margin-bottom:15px;">🌍 Travel Gallery</h1>

<p style="font-size:16.5px; color:#555; text-align:center; max-width:750px; margin:0 auto 25px;">
A curated collection of my travel memories — moments and stories from different cities and countries around the world.
</p>

<!-- ===================
 🔗 自动导航菜单（根据每个 section 自动生成）
=================== -->
<div id="dynamic-nav"></div>

<hr style="margin-top:10px; margin-bottom:35px;">


<!-- ===================
 🇩🇰 Denmark
=================== -->
<section id="denmark" class="travel-block" data-country="🇩🇰 Denmark" style="--accent-color:#d63031; --bg1:#fff6f6; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇩🇰 Nov 2022 – Denmark Memories</h2>
    <p>Discovering Copenhagen’s colorful harbors, cozy streets, and the warmth of hygge in winter light.</p>
  </div>

  <div class="gallery">
    {% for i in (1..20) %}
      <img src="{{ site.baseurl }}/images/travel/2022/dec_denmark/2022_denmark_{{ i }}.jpg" alt="Denmark photo {{ i }}">
    {% endfor %}
  </div>
</section>


<!-- ===================
 🇮🇹 Italy
=================== -->
<section id="italy" class="travel-block" data-country="🇮🇹 Italy" style="--accent-color:#c0392b; --bg1:#fff5f2; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇮🇹 Oct 2022 – Italy Memories</h2>
    <p>Wandering through Rome’s ancient ruins and Venice’s serene canals — a journey through time and beauty.</p>
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
<section id="france" class="travel-block" data-country="🇫🇷 France" style="--accent-color:#e67e22; --bg1:#fff9f0; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇫🇷 Sep 2022 – France Memories</h2>
    <p>From the Louvre to the Eiffel Tower — art, architecture, and the rhythm of Paris nights.</p>
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
<section id="germany" class="travel-block" data-country="🇩🇪 Germany" style="--accent-color:#007acc; --bg1:#f0f8ff; --bg2:#fff;">
  <div class="travel-header">
    <h2>🇩🇪 Aug 2022 – Germany Memories</h2>
    <p>Exploring Berlin’s vibrant streets and Hamburg’s peaceful waterways — where history meets modern charm.</p>
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

<!-- ========= 自动生成导航栏 ========= -->
<script>
document.addEventListener("DOMContentLoaded", function() {
  const navContainer = document.getElementById("dynamic-nav");
  const sections = document.querySelectorAll("section[data-country]");
  let navHTML = '<nav class="travel-nav">';
  sections.forEach(sec => {
    const id = sec.getAttribute("id");
    const name = sec.getAttribute("data-country");
    navHTML += `<a href="#${id}">${name}</a>`;
  });
  navHTML += '</nav>';
  navContainer.innerHTML = navHTML;
});
</script>

<!-- ========= 样式部分 ========= -->
<style>
/* ========= 自动导航条 ========= */
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

/* ========= Section 样式 ========= */
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

/* ========= Gallery（瀑布流布局） ========= */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-gap: 12px;
  margin-top: 10px;
  align-items: start;
}

/* 原比例展示，不失真 */
.gallery img {
  width: 100%;
  height: auto;
  border-radius: 10px;
  object-fit: contain;
  background: #f8f8f8;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* 鼠标悬停效果 */
.gallery img:hover {
  transform: scale(1.03);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
}

/* ========= 响应式布局 ========= */
@media (max-width: 900px) {
  .gallery { grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); }
}
@media (max-width: 600px) {
  .gallery { grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); }
}
</style>
