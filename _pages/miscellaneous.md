---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<!-- 顶部阅读进度条 -->
<div id="progress-bar"></div>

<h1 id="top" style="text-align:center; margin-bottom:15px; opacity:0; transform:translateY(-12px); animation:fadeSlide 1.0s ease-out forwards;">
  🌍 Travel Gallery
</h1>
<p style="font-size:16px; text-align:center; margin-bottom:40px; color:#555;">
  A collection of travel memories — each place tells a story of moments, light, and time.
</p>

<!-- ======================
导航栏 + 搜索框 + 时间轴
====================== -->
<nav id="gallery-nav"></nav>

<!-- 搜索输入框 -->
<div id="search-bar" style="text-align:center; margin:10px 0;">
  <input type="text" id="country-search" placeholder="🔍 Search by country or keyword..." 
         style="padding:8px 14px; width:60%; max-width:400px; border:1px solid #ccc; border-radius:8px; font-size:15px;">
</div>

<!-- 无结果提示 -->
<p id="no-result" style="display:none; text-align:center; color:#999; margin:20px 0;">No matching results 😢</p>

<div class="timeline"></div>

<!-- ======================
🇩🇰 Denmark
====================== -->
<div class="country-section" data-country="Denmark" data-flag="🇩🇰" style="--theme1:#8e44ad; --theme2:#f3e5f5;">
  <div class="country-header">
    <h3 class="toggle">🇩🇰 Nov. 2022 – Denmark Memories</h3>
    <p>Where warmth meets simplicity — Copenhagen’s colors in the northern light.</p>
  </div>
  <p class="photo-desc">Nyhavn reflections, winter walks, and Danish hygge at dusk.</p>
  <div class="gallery">
    {% for i in (1..36) %}
      <a href="{{ site.baseurl }}/images/travel/2022/nov_denmark/2022_denmark_{{ i }}.jpg"
         class="glightbox"
         data-gallery="denmark"
         data-title="Denmark — Scene {{ i }}">
        <img loading="lazy"
             src="{{ site.baseurl }}/images/travel/2022/nov_denmark/2022_denmark_{{ i }}.jpg"
             alt="Denmark photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <p class="download-link">
    <a href="{{ site.baseurl }}/images/travel/2022/nov_denmark/denmark_memories.zip" download>⬇️ Download Denmark Album</a>
  </p>
</div>

<!-- ======================
🇮🇹 Italy
====================== -->
<div class="country-section" data-country="Italy" data-flag="🇮🇹" style="--theme1:#c0392b; --theme2:#fbe9e7;">
  <div class="country-header">
    <h3 class="toggle">🇮🇹 Oct. 2022 – Italy Memories</h3>
    <p>Exploring Rome, Florence, and Venice — cities of timeless art and gentle light.</p>
  </div>
  <p class="photo-desc">Scenes from Rome’s ruins, Venice’s canals, and Florence’s sunsets.</p>
  <div class="gallery">
    {% for i in (1..12) %}
      <a href="{{ site.baseurl }}/images/travel/2022/oct_italy/2022_italy_{{ i }}.jpg"
         class="glightbox"
         data-gallery="italy"
         data-title="Italy — Moment {{ i }}">
        <img loading="lazy"
             src="{{ site.baseurl }}/images/travel/2022/oct_italy/2022_italy_{{ i }}.jpg"
             alt="Italy photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <p class="download-link">
    <a href="{{ site.baseurl }}/images/travel/2022/oct_italy/italy_memories.zip" download>⬇️ Download Italy Album</a>
  </p>
</div>

<!-- ======================
🇫🇷 France
====================== -->
<div class="country-section" data-country="France" data-flag="🇫🇷" style="--theme1:#d35400; --theme2:#fff3e0;">
  <div class="country-header">
    <h3 class="toggle">🇫🇷 Sep. 2022 – France Memories</h3>
    <p>Paris mornings, Lyon evenings — beauty in light, architecture, and rhythm.</p>
  </div>
  <p class="photo-desc">From the Eiffel Tower to quiet Paris streets and Provençal charm.</p>
  <div class="gallery">
    {% for i in (1..28) %}
      <a href="{{ site.baseurl }}/images/travel/2022/sep_france/2022_france_{{ i }}.jpg"
         class="glightbox"
         data-gallery="france"
         data-title="France — Moment {{ i }}">
        <img loading="lazy"
             src="{{ site.baseurl }}/images/travel/2022/sep_france/2022_france_{{ i }}.jpg"
             alt="France photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <p class="download-link">
    <a href="{{ site.baseurl }}/images/travel/2022/sep_france/france_memories.zip" download>⬇️ Download France Album</a>
  </p>
</div>

<!-- ======================
🇩🇪 Germany
====================== -->
<div class="country-section" data-country="Germany" data-flag="🇩🇪" style="--theme1:#2980b9; --theme2:#e3f2fd;">
  <div class="country-header">
    <h3 class="toggle">🇩🇪 Aug. 2022 – Germany Memories</h3>
    <p>Berlin’s energy and Munich’s calm — stories written in streets and rivers.</p>
  </div>
  <p class="photo-desc">Berlin walls, Hamburg harbors, and summer nights by the Rhine.</p>
  <div class="gallery">
    {% for i in (1..36) %}
      <a href="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg"
         class="glightbox"
         data-gallery="germany"
         data-title="Germany — Memory {{ i }}">
        <img loading="lazy"
             src="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg"
             alt="Germany photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <p class="download-link">
    <a href="{{ site.baseurl }}/images/travel/2022/aug_germany/germany_memories.zip" download>⬇️ Download Germany Album</a>
  </p>
</div>

<!-- 联系方式 -->
<hr style="margin-top:60px; margin-bottom:10px;">
<p style="text-align:center; margin-top:40px; color:#555; font-size:15px;">
  📧 Contact: <a href="mailto:zhichen.colin@gmail.com" style="color:#2980b9; text-decoration:none;">zhichen.colin@gmail.com</a>
</p>

<!-- 返回顶部按钮 -->
<button id="go-top" title="Back to Top">↑</button>

<!-- CSS -->
<link rel="stylesheet" href="{{ '/assets/css/glightbox.min.css' | relative_url }}">
<style>
#progress-bar{position:fixed;top:0;left:0;height:4px;width:0;
  background:linear-gradient(90deg,#2980b9,#8e44ad);z-index:200;}
#gallery-nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,0.96);
  backdrop-filter:blur(6px);text-align:center;padding:10px;border-bottom:1px solid #ddd;margin-bottom:8px;transition:box-shadow .3s ease;}
#gallery-nav.shadow{box-shadow:0 2px 8px rgba(0,0,0,.1);}
#gallery-nav a{display:inline-block;margin:0 6px;padding:8px 14px;border-radius:8px;
  font-weight:600;background:#f4f4f4;color:#333;text-decoration:none;transition:all .3s ease;}
#gallery-nav a.active,#gallery-nav a:hover{background:#333;color:#fff;}
#go-top{position:fixed;bottom:30px;right:30px;background:#2980b9;color:white;
  border:none;border-radius:50%;width:44px;height:44px;font-size:18px;
  box-shadow:0 4px 12px rgba(0,0,0,.2);opacity:0;pointer-events:none;transition:all .3s;}
#go-top.show{opacity:1;pointer-events:auto;}
#go-top:hover{transform:scale(1.1);}
.country-section{position:relative;
  background:linear-gradient(180deg,var(--theme2) 0%,#fff 100%);
  border-radius:14px;padding:25px 20px;margin-bottom:60px;
  box-shadow:0 2px 10px rgba(0,0,0,.05);}
.country-section::before{content:"";display:block;height:6px;
  border-radius:6px 6px 0 0;
  background:linear-gradient(90deg,var(--theme1),#fff,var(--theme2));
  position:absolute;left:0;right:0;top:0;}
.download-link{text-align:center;margin:8px 0;}
.download-link a{background:#2980b9;color:#fff;padding:8px 14px;border-radius:8px;text-decoration:none;font-size:14px;}
.download-link a:hover{background:#1f5f87;}
</style>

<!-- JS -->
<script src="{{ '/assets/js/glightbox.min.js' | relative_url }}"></script>
<script>
window.addEventListener("load",()=>{
  // 自动生成导航（含国旗）
  const nav=document.getElementById("gallery-nav");
  const sections=[...document.querySelectorAll(".country-section")];
  sections.forEach(sec=>{
    const name=sec.dataset.country;
    const flag=sec.dataset.flag || "";
    const id=name.toLowerCase();
    sec.id=id;
    const a=document.createElement("a");
    a.href=`#${id}`;
    a.textContent=`${flag} ${name}`;
    nav.appendChild(a);
  });

  // 滚动阴影
  window.addEventListener("scroll",()=>{
    document.getElementById("gallery-nav").classList.toggle("shadow",window.scrollY>60);
    goTop.classList.toggle("show",window.scrollY>400);
  });

  // 返回顶部按钮
  const goTop=document.getElementById("go-top");
  goTop.addEventListener("click",()=>window.scrollTo({top:0,behavior:"smooth"}));

  // Lightbox
  GLightbox({ selector:'.glightbox', loop:true, touchNavigation:true });
});
</script>
