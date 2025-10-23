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

<div class="timeline"></div>

<!-- ======================
🇩🇰 Denmark
====================== -->
<div class="country-section" data-country="Denmark" style="--theme1:#8e44ad; --theme2:#f3e5f5;">
  <div class="country-header">
    <h3 class="toggle">Nov. 2022 – Denmark Memories</h3>
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
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<!-- ======================
🇮🇹 Italy
====================== -->
<div class="country-section" data-country="Italy" style="--theme1:#c0392b; --theme2:#fbe9e7;">
  <div class="country-header">
    <h3 class="toggle">Oct. 2022 – Italy Memories</h3>
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
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<!-- ======================
🇫🇷 France
====================== -->
<div class="country-section" data-country="France" style="--theme1:#d35400; --theme2:#fff3e0;">
  <div class="country-header">
    <h3 class="toggle">Sep. 2022 – France Memories</h3>
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
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<!-- ======================
🇩🇪 Germany
====================== -->
<div class="country-section" data-country="Germany" style="--theme1:#2980b9; --theme2:#e3f2fd;">
  <div class="country-header">
    <h3 class="toggle">Aug. 2022 – Germany Memories</h3>
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
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<hr style="margin-top:60px; margin-bottom:10px;">
<p style="text-align:center; margin-top:40px; color:#555; font-size:15px;">
  📧 Contact: <a href="mailto:zhichen.colin@gmail.com" style="color:#2980b9; text-decoration:none;">zhichen.colin@gmail.com</a>
</p>

<!-- ======================
加载动画
====================== -->
<div id="loading-overlay" 
     style="position:fixed; inset:0; background:white; display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:9999; font-size:18px; color:#555; transition:opacity .6s ease;">
  <div class="spinner" style="width:40px; height:40px; border:4px solid #ccc; border-top:4px solid #2980b9; border-radius:50%; animation:spin 1s linear infinite;"></div>
  <p style="margin-top:15px;">Loading gallery...</p>
</div>

<!-- ======================
CSS 样式
====================== -->
<link rel="stylesheet" href="{{ '/assets/css/glightbox.min.css' | relative_url }}">
<style>
@keyframes spin { to { transform:rotate(360deg); } }
#progress-bar{ position:fixed; top:0; left:0; height:4px; width:0;
  background:linear-gradient(90deg,#2980b9,#8e44ad); z-index:200; }

#gallery-nav{ position:sticky; top:0; z-index:100; background:rgba(255,255,255,0.96);
  backdrop-filter:blur(6px); text-align:center; padding:10px; border-bottom:1px solid #ddd; margin-bottom:8px; }
#gallery-nav a{ display:inline-block; margin:0 8px; padding:8px 14px; border-radius:8px;
  font-weight:600; background:#f4f4f4; color:#333; text-decoration:none; transition:all .3s ease; }
#gallery-nav a.active,#gallery-nav a:hover{ background:#333; color:#fff; }

#country-search:focus { outline:none; border-color:#2980b9; box-shadow:0 0 6px rgba(41,128,185,.3); }

.timeline{ display:flex; justify-content:center; gap:10px; flex-wrap:wrap; font-size:14px; color:#666; margin-bottom:22px; }
.timeline span{ background:#f9f9f9; padding:6px 12px; border-radius:8px; }

.country-section{ position:relative; background:linear-gradient(180deg,var(--theme2) 0%,#fff 100%);
  border-radius:14px; padding:25px 20px; margin-bottom:60px; box-shadow:0 2px 10px rgba(0,0,0,.05); }
.country-section::before{ content:""; display:block; height:5px; border-radius:5px 5px 0 0;
  background:linear-gradient(90deg,var(--theme1),var(--theme2)); position:absolute; left:0; right:0; top:0; }

.country-header h3{ color:var(--theme1); font-size:20px; margin:0 0 6px; font-weight:700; cursor:pointer; user-select:none; }
.photo-desc{ font-style:italic; color:#666; margin:4px 0 16px; text-align:center; }

.gallery{ column-count:3; column-gap:15px; }
.gallery a{ position:relative; display:inline-block; break-inside:avoid; }
.gallery img{ width:100%; height:auto; border-radius:8px; margin-bottom:15px;
  opacity:0; transform:translateY(15px); transition:all .8s ease; }
.gallery img.visible{ opacity:1; transform:translateY(0); }
.gallery img:hover{ transform:scale(1.03); box-shadow:0 4px 12px rgba(0,0,0,.2); }

.back-top{ text-align:right; margin-top:6px; }
.back-top a{ font-size:14px; color:#666; text-decoration:none; }
.back-top a:hover{ color:var(--theme1); }

@keyframes fadeSlide{ to{ opacity:1; transform:translateY(0);} }
@media(max-width:1000px){ .gallery{ column-count:2; } }
@media(max-width:700px){ .gallery{ column-count:1; } }
</style>

<!-- ======================
JS 脚本
====================== -->
<script src="{{ '/assets/js/glightbox.min.js' | relative_url }}"></script>
<script>
window.addEventListener("load",()=>{
  // Loading 动画淡出
  const overlay=document.getElementById("loading-overlay");
  setTimeout(()=>{ overlay.style.opacity=0; setTimeout(()=>overlay.remove(),600); },1000);

  // 自动生成导航
  const nav=document.getElementById("gallery-nav");
  const sections=[...document.querySelectorAll(".country-section")];
  sections.forEach(sec=>{
    const name=sec.dataset.country; const id=name.toLowerCase();
    sec.id=id;
    const a=document.createElement("a"); a.href=`#${id}`; a.textContent=name;
    nav.appendChild(a);
  });

  // 时间轴
  const timeline=document.querySelector(".timeline");
  ["Aug 🇩🇪","Sep 🇫🇷","Oct 🇮🇹","Nov 🇩🇰"].forEach(m=>{
    const s=document.createElement("span"); s.textContent=m; timeline.appendChild(s);
  });

  // 搜索功能
  const input=document.getElementById("country-search");
  input.addEventListener("input",()=>{
    const val=input.value.trim().toLowerCase();
    sections.forEach(sec=>{
      const text=sec.textContent.toLowerCase();
      sec.style.display=(text.includes(val)) ? "" : "none";
    });
  });

  // 图片计数
  sections.forEach(sec=>{
    const imgs=sec.querySelectorAll(".gallery img");
    const h3=sec.querySelector(".country-header h3");
    if(imgs.length && h3){
      const span=document.createElement("span");
      span.textContent=`（共${imgs.length}张）`;
      span.style.fontSize="14px"; span.style.color="#777"; span.style.marginLeft="8px";
      h3.appendChild(span);
    }
  });

  // 平滑滚动
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener("click",e=>{
      e.preventDefault();
      document.querySelector(a.getAttribute("href")).scrollIntoView({behavior:"smooth"});
    });
  });

  // ScrollSpy 导航高亮
  const navLinks=[...document.querySelectorAll('#gallery-nav a')];
  const spy=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        navLinks.forEach(l=>l.classList.remove('active'));
        const current=document.querySelector(`#gallery-nav a[href="#${entry.target.id}"]`);
        current && current.classList.add('active');
      }
    });
  },{threshold:0.3, rootMargin:"-20% 0px -60% 0px"});
  sections.forEach(sec=>spy.observe(sec));

  // 图片淡入动画
  const imgs=document.querySelectorAll('.gallery img');
  const fadeIn=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){ e.target.classList.add('visible'); fadeIn.unobserve(e.target); }
    });
  });
  imgs.forEach(img=>fadeIn.observe(img));

  // 折叠/展开
  document.querySelectorAll('.country-header .toggle').forEach(h3=>{
    h3.addEventListener('click',()=>{
      const gal=h3.parentElement.parentElement.querySelector('.gallery');
      gal.style.display = (gal.style.display==='none' ? '' : 'none');
    });
  });

  // Lightbox 初始化
  GLightbox({ selector:'.glightbox', loop:true, touchNavigation:true });

  // 阅读进度条
  const bar=document.getElementById('progress-bar');
  const update=()=>{
    const max=document.body.scrollHeight - window.innerHeight;
    const pct=max>0?(window.scrollY/max)*100:0;
    bar.style.width=pct+'%';
  };
  update(); window.addEventListener('scroll',update);
});
</script>
