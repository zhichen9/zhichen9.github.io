---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<h1 id="top" style="text-align:center; margin-bottom:15px;">🌍 Travel Gallery</h1>
<p style="font-size:16px; text-align:center; margin-bottom:40px; color:#555;">
A collection of travel memories — each place tells a story of moments, light, and time.
</p>

<nav id="gallery-nav"></nav>
<div class="timeline"></div>

<!-- 🇩🇰 Denmark -->
<div class="country-section" data-country="Denmark" style="--theme1:#8e44ad; --theme2:#f3e5f5;">
  <div class="country-header">
    <h3>Nov. 2022 – Denmark Memories</h3>
    <p>Where warmth meets simplicity — Copenhagen’s colors in the northern light.</p>
  </div>
  <p class="photo-desc">Nyhavn reflections, winter walks, and Danish hygge at dusk.</p>
  <div class="gallery">
    {% for i in (1..36) %}
      <a href="{{ site.baseurl }}/images/travel/2022/nov_denmark/2022_denmark_{{ i }}.jpg"
         class="glightbox"
         data-gallery="denmark"
         data-title="Denmark – Scene {{ i }}">
         <img src="{{ site.baseurl }}/images/travel/2022/nov_denmark/2022_denmark_{{ i }}.jpg" alt="Denmark photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<!-- 🇮🇹 Italy -->
<div class="country-section" data-country="Italy" style="--theme1:#c0392b; --theme2:#fbe9e7;">
  <div class="country-header">
    <h3>Oct. 2022 – Italy Memories</h3>
    <p>Exploring Rome, Florence, and Venice — cities of timeless art and gentle light.</p>
  </div>
  <p class="photo-desc">Scenes from Rome’s ruins, Venice’s canals, and Florence’s sunsets.</p>
  <div class="gallery">
    {% for i in (1..12) %}
      <a href="{{ site.baseurl }}/images/travel/2022/oct_italy/2022_italy_{{ i }}.jpg"
         class="glightbox"
         data-gallery="italy"
         data-title="Italy – Moment {{ i }}">
         <img src="{{ site.baseurl }}/images/travel/2022/oct_italy/2022_italy_{{ i }}.jpg" alt="Italy photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<!-- 🇫🇷 France -->
<div class="country-section" data-country="France" style="--theme1:#d35400; --theme2:#fff3e0;">
  <div class="country-header">
    <h3>Sep. 2022 – France Memories</h3>
    <p>Paris mornings, Lyon evenings — beauty in light, architecture, and rhythm.</p>
  </div>
  <p class="photo-desc">From the Eiffel Tower to quiet Paris streets and Provençal charm.</p>
  <div class="gallery">
    {% for i in (1..28) %}
      <a href="{{ site.baseurl }}/images/travel/2022/sep_france/2022_france_{{ i }}.jpg"
         class="glightbox"
         data-gallery="france"
         data-title="France – Moment {{ i }}">
         <img src="{{ site.baseurl }}/images/travel/2022/sep_france/2022_france_{{ i }}.jpg" alt="France photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<!-- 🇩🇪 Germany -->
<div class="country-section" data-country="Germany" style="--theme1:#2980b9; --theme2:#e3f2fd;">
  <div class="country-header">
    <h3>Aug. 2022 – Germany Memories</h3>
    <p>Berlin’s energy and Munich’s calm — stories written in streets and rivers.</p>
  </div>
  <p class="photo-desc">Berlin walls, Hamburg harbors, and summer nights by the Rhine.</p>
  <div class="gallery">
    {% for i in (1..36) %}
      <a href="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg"
         class="glightbox"
         data-gallery="germany"
         data-title="Germany – Memory {{ i }}">
         <img src="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg" alt="Germany photo {{ i }}">
      </a>
    {% endfor %}
  </div>
  <div class="back-top"><a href="#top">↑ Back to Top</a></div>
</div>

<hr style="margin-top:60px; margin-bottom:10px;">
<p style="text-align:center;">
<b>Email:</b> <a href="mailto:zhichen.colin@gmail.com">zhichen.colin@gmail.com</a>
</p>

<!-- 样式 -->
<link rel="stylesheet" href="{{ '/assets/css/glightbox.min.css' | relative_url }}">
<style>
#gallery-nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,0.96);backdrop-filter:blur(6px);text-align:center;padding:10px;border-bottom:1px solid #ddd;margin-bottom:15px;}
#gallery-nav a{display:inline-block;margin:0 8px;padding:8px 14px;border-radius:8px;font-weight:600;background:#f4f4f4;color:#333;text-decoration:none;transition:all 0.3s ease;}
#gallery-nav a.active,#gallery-nav a:hover{background:#333;color:#fff;}
.timeline{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;font-size:14px;color:#666;margin-bottom:25px;}
.timeline span{background:#f9f9f9;padding:6px 12px;border-radius:8px;}
.country-section{background:linear-gradient(180deg,var(--theme2) 0%,#fff 100%);border-radius:14px;padding:25px 20px;margin-bottom:60px;box-shadow:0 2px 10px rgba(0,0,0,0.05);}
.country-header h3{color:var(--theme1);font-size:20px;margin:0 0 5px;font-weight:700;}
.country-header p{margin:0 0 10px;color:#555;font-size:15px;}
.photo-desc{font-style:italic;color:#666;margin:6px 0 18px;text-align:center;}
.gallery{column-count:3;column-gap:15px;}
.gallery a{display:inline-block;}
.gallery img{width:100%;height:auto;border-radius:8px;margin-bottom:15px;break-inside:avoid;opacity:0;transform:translateY(15px);transition:all 0.8s ease;}
.gallery img.visible{opacity:1;transform:translateY(0);}
.gallery img:hover{transform:scale(1.03);box-shadow:0 4px 12px rgba(0,0,0,0.2);}
.back-top{text-align:right;margin-top:10px;}
.back-top a{font-size:14px;color:#666;text-decoration:none;}
.back-top a:hover{color:var(--theme1);}
@media(max-width:1000px){.gallery{column-count:2;}}
@media(max-width:700px){.gallery{column-count:1;}}
</style>

<script src="{{ '/assets/js/glightbox.min.js' | relative_url }}"></script>
<script>
document.addEventListener("DOMContentLoaded",()=>{
  const nav=document.getElementById("gallery-nav");
  const sections=document.querySelectorAll(".country-section");
  sections.forEach(sec=>{
    const name=sec.dataset.country;
    const id=name.toLowerCase();
    sec.id=id;
    const link=document.createElement("a");
    link.href=`#${id}`;
    link.textContent=name;
    nav.appendChild(link);
  });

  const timeline=document.querySelector(".timeline");
  const months=["Aug 🇩🇪","Sep 🇫🇷","Oct 🇮🇹","Nov 🇩🇰"];
  months.forEach(m=>{
    const span=document.createElement("span");
    span.textContent=m;
    timeline.appendChild(span);
  });

  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener("click",e=>{
      e.preventDefault();
      document.querySelector(a.getAttribute("href")).scrollIntoView({behavior:"smooth"});
    });
  });

  const navLinks=document.querySelectorAll('#gallery-nav a');
  const spy=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        navLinks.forEach(l=>l.classList.remove('active'));
        document.querySelector(`#gallery-nav a[href="#${entry.target.id}"]`)?.classList.add('active');
      }
    });
  },{threshold:0.5});
  sections.forEach(sec=>spy.observe(sec));

  const imgs=document.querySelectorAll('.gallery img');
  const fadeIn=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('visible');
        fadeIn.unobserve(e.target);
      }
    });
  });
  imgs.forEach(img=>fadeIn.observe(img));

  /* 初始化灯箱 */
  const lightbox=GLightbox({
    selector:'.glightbox',
    loop:true,
    touchNavigation:true,
    closeButton:true,
    plyr:{css:false,js:false}
  });
});
</script>
