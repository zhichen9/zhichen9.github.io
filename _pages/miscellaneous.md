---
layout: archive
title: "Miscellaneous"
permalink: /miscellaneous/
author_profile: false
body_class: misc-gallery-page
markdown: false
---

{%- assign data = site.data.travel.descriptions -%}
{%- assign meta = site.data.travel.section_meta -%}

<!-- Title + Intro -->
<h2 id="top" class="gallery-title">
  Travel Gallery
</h2>

<p class="gallery-intro">
  <em>
    Welcome to my gallery! Here are a few snapshots from my academic life and personal journey.<br>
    A collection of travel memories — each place tells a story of moments, light, and time.
  </em>
</p>

<nav id="gallery-nav"></nav>

<div id="search-bar" style="text-align:center;margin:10px 0 2px;">
  <input id="country-search" type="text" placeholder="Search country or keyword..."
         style="padding:8px 14px;width:60%;max-width:420px;border:1px solid #ccc;border-radius:8px;font-size:15px;">
</div>
<p id="no-result" style="display:none;text-align:center;color:#999;margin:10px 0 16px;">No matching results.</p>

<!-- Countries -->
{%- assign sections = 
  "dec_finland|fi|Finland|#003580|11|2022|Dec,/downloads/finland.zip;
   nov_denmark|dk|Denmark|#C60C30|36|2022|Nov,/downloads/denmark.zip;
   oct_italy|it|Italy|#008C45|12|2022|Oct,/downloads/italy.zip;
   sep_france|fr|France|#0055A4|28|2022|Sep,/downloads/france.zip;
   aug_germany|de|Germany|#000000|36|2022|Aug,/downloads/germany.zip" 
   | split: ";" -%}

{%- for raw in sections -%}
  {%- assign parts = raw | strip | split: "," -%}
  {%- assign left = parts[0] | split: "|" -%}
  {%- assign key = left[0] | strip -%}
  {%- assign flag = left[1] | strip -%}
  {%- assign cname = left[2] | strip -%}
  {%- assign theme = left[3] | strip -%}
  {%- assign total = left[4] | plus: 0 -%}
  {%- assign year = left[5] | strip -%}
  {%- assign month = left[6] | strip -%}
  {%- assign dl = parts[1] | strip -%}
  {%- assign cname_lower = cname | downcase -%}
  {%- assign photos = data[key] -%}
  {%- assign secmeta = meta[key] -%}

  <div class="country-section" data-country="{{ cname }}" style="--theme1:{{ theme }};--theme2:#f7f9ff;">
    <div class="country-header">
      <div class="country-heading">
        <img class="country-flag"
             src="https://flagcdn.com/w40/{{ flag }}.png"
             alt="{{ cname }} flag"
             width="28"
             height="21"
             loading="lazy">
        <h3 class="toggle">{{ month }}. {{ year }} – {{ cname }} Memories</h3>
      </div>

      {%- if secmeta and secmeta.summary_en -%}
        <p class="section-summary">{{ secmeta.summary_en }}</p>
      {%- else -%}
        <p class="section-summary">Scenes from {{ cname }} — light, rhythm, and color in every frame.</p>
      {%- endif -%}

      {%- if secmeta and secmeta.subtitle_en -%}
        <p class="section-subtitle">{{ secmeta.subtitle_en }}</p>
      {%- endif -%}
    </div>

    <p class="photo-desc">Click a photo to open full view. Use EN / 中文 to switch captions.</p>

    <div class="gallery">
      {%- for i in (1..total) -%}
        {%- assign p = photos | where: "id", i | first -%}
        {%- if p -%}
        {%- assign title = p.title_en | default: cname | append: " — Scene " | append: i -%}

        <a href="{{ site.baseurl }}/images/travel/{{ year }}/{{ key }}/{{ year }}_{{ cname_lower }}_{{ i }}.jpg"
           class="glightbox"
           data-gallery="{{ key }}"
           data-title="{{ title }}"
           data-caption-date="{{ p.date }}"
           data-caption-location-en="{{ p.location_en }}"
           data-caption-location-zh="{{ p.location_zh }}"
           data-caption-place-en="{{ p.landmark_en }}"
           data-caption-place-zh="{{ p.landmark_zh }}"
           data-caption-desc-en="{{ p.description_en }}"
           data-caption-desc-zh="{{ p.description_zh }}">
          <img loading="lazy"
               src="{{ site.baseurl }}/images/travel/{{ year }}/{{ key }}/{{ year }}_{{ cname_lower }}_{{ i }}.jpg"
               alt="{{ title }}">
        </a>
        {%- endif -%}
      {%- endfor -%}
    </div>

    <p class="download-link">
      <a href="{{ dl }}" download>Download {{ cname }} Album ({{ total }} photos)</a>
    </p>
    <div class="back-top"><a href="#top">↑ Back to Top</a></div>
  </div>
{%- endfor -%}

<hr style="margin-top:56px;margin-bottom:10px;">
<p style="text-align:center;margin-top:10px;color:#555;font-size:15px;">
  Contact: <a href="mailto:zhichen.colin@gmail.com" style="color:#2980b9;text-decoration:none;">zhichen.colin@gmail.com</a>
</p>

<button id="go-top" title="Back to Top">↑</button>

<link rel="stylesheet" href="{{ '/assets/css/glightbox.min.css' | relative_url }}">

<style>
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes fadeSlide{to{opacity:1;transform:translateY(0)}}

#gallery-nav{
  position:sticky;top:0;z-index:100;
  background:var(--site-bg,#fff);
  text-align:left;
  padding:8px 0;
  border-top:1px solid var(--site-border,#e6e6e6);
  border-bottom:1px solid var(--site-border,#e6e6e6)
}
#gallery-nav.shadow{box-shadow:none}
#gallery-nav a{
  display:inline-block;margin:0 18px 0 0;padding:0;
  background:transparent;color:var(--site-link,#0645ad);text-decoration:none;font-weight:400
}
#gallery-nav a.active,#gallery-nav a:hover{text-decoration:underline;background:transparent;color:var(--site-link-hover,#000)}

#country-search:focus{
  outline:none;border-color:#777;box-shadow:none
}

.country-section{
  position:relative;
  background:transparent;
  border-radius:0;
  padding:0;
  margin:32px 0 44px;
  box-shadow:none;
  border-top:1px solid var(--site-border,#e6e6e6)
}
.country-section::before{display:none}

.country-heading{
  display:flex;
  align-items:center;
  gap:10px;
  margin:14px 0 8px
}
.country-flag{
  width:28px;
  height:21px;
  object-fit:cover;
  border:1px solid var(--site-border,#e6e6e6);
  flex-shrink:0
}
.country-header h3{
  color:var(--site-text,#222);font-size:1.15em;margin:0;font-weight:700;cursor:pointer
}
.section-summary{
  margin:6px 0 8px;
  color:var(--site-muted,#666);
  font-size:1em;
  line-height:1.6;
  text-align:left;
}
.section-subtitle{
  margin:0 0 12px;
  color:var(--site-muted,#666);
  font-size:0.95em;
  line-height:1.7;
  text-align:left;
  font-style:italic;
}

.photo-desc{
  font-style:italic;color:var(--site-muted,#666);margin:2px 0 14px;text-align:left
}

.gallery{column-count:3;column-gap:15px}
.gallery a{position:relative;display:inline-block;break-inside:avoid}
.gallery img{
  width:100%;height:auto;border-radius:0;margin-bottom:15px;
  opacity:1;transform:none;transition:opacity .2s ease
}
.gallery img.visible{opacity:1;transform:none}
.gallery img:hover{
  transform:none;
  opacity:.9;
  box-shadow:none;
  will-change:transform
}

.download-link{text-align:center;margin:8px 0}
.download-link a{
  background:transparent;color:var(--site-link,#0645ad);padding:0;border-radius:0;
  text-decoration:underline;font-size:0.95em
}
.download-link a:hover{background:transparent;color:var(--site-link-hover,#000)}

.back-top{text-align:right;margin-top:8px}
.back-top a{font-size:14px;color:#777;text-decoration:none}
.back-top a:hover{color:var(--theme1)}

#go-top{
  position:fixed;bottom:30px;right:30px;background:var(--site-bg,#fff);color:var(--site-link,#0645ad);border:1px solid var(--site-border,#e6e6e6);
  border-radius:0;width:34px;height:34px;font-size:16px;
  box-shadow:none;
  opacity:0;pointer-events:none;transition:all .3s
}
#go-top.show{opacity:1;pointer-events:auto}
#go-top:hover{text-decoration:underline;transform:none}

.glightbox-container .gslide.current{
  display:flex!important;
  flex-direction:column!important;
  justify-content:center!important;
  align-items:center!important;
  max-height:100vh
}
.glightbox-container .gslide-media{
  flex:1 1 auto;
  display:flex!important;
  align-items:center!important;
  justify-content:center!important;
  max-height:calc(100vh - 150px);
  width:100%
}
.glightbox-container .gslide-image img{
  max-height:calc(100vh - 150px)!important;
  width:auto!important;
  object-fit:contain
}
.glightbox-container .gslide-title{
  display:none!important
}
.glightbox-container .gslide-description{
  position:relative!important;
  left:auto!important;
  right:auto!important;
  bottom:auto!important;
  flex:0 0 auto;
  width:100%;
  background:#fff!important;
  max-height:none;
  overflow:visible;
  padding:16px 24px 20px;
  border-top:1px solid #e6e6e6;
  box-shadow:0 -4px 18px rgba(0,0,0,0.06)
}
.gdesc-inner{
  background:transparent!important;
  color:#222!important;
  border-radius:0;padding:0;
  line-height:1.55;font-size:14px;max-width:920px;margin:0 auto
}
.caption-panel{
  text-align:center;
  font-family:Georgia,"Times New Roman",serif
}
.caption-panel__title{
  margin:0 0 10px;
  font-size:17px;
  font-weight:700;
  color:#111;
  line-height:1.35
}
.caption-panel__meta{
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:6px 14px;
  margin:0 0 8px;
  font-size:13px;
  color:#555;
  line-height:1.5;
  font-family:Arial,Helvetica,sans-serif
}
.caption-panel__meta-item strong{
  font-weight:600;
  color:#333
}
.caption-panel__text{
  margin:10px auto 0;
  max-width:760px;
  font-size:14px;
  line-height:1.65;
  color:#444;
  font-style:italic
}
.glightbox-open #lang-toggle{
  z-index:1000001;
  top:12px;
  right:12px
}

#lang-toggle{
  position:fixed;top:10px;right:10px;background:var(--site-bg,#fff);color:var(--site-link,#0645ad);font-size:13px;
  border:1px solid var(--site-border,#e6e6e6);border-radius:0;padding:4px 8px;z-index:9999;cursor:pointer;
  box-shadow:none
}
#lang-toggle:hover{text-decoration:underline;background:var(--site-bg,#fff)}

@media(max-width:680px){
  .glightbox-container .gslide-description{padding:14px 16px 18px}
  .caption-panel__title{font-size:15px}
  .caption-panel__meta{
    flex-direction:column;
    gap:4px
  }
}

.caption-block{
  text-align:left;line-height:1.7;
  font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif
}
.caption-meta{
  font-size:14px;color:#444;margin-bottom:4px
}
.caption-text{
  margin-top:10px;font-size:15px;color:#222;font-style:italic
}

.gallery-intro{
  text-align:left;color:var(--site-muted,#666);font-size:1em;line-height:1.6;letter-spacing:0;
  font-style:italic;margin:0 0 18px;
  font-family:Arial, Helvetica, sans-serif
}

.gallery-title{
  margin:0 0 12px;
  padding-bottom:0.1em;
  border-bottom:1px solid var(--site-border,#e6e6e6);
  font-size:1.15em;
  line-height:1.25;
  font-weight:700
}

@media(max-width:1000px){.gallery{column-count:2}}
@media(max-width:680px){
  .gallery{column-count:1}
  .section-summary,
  .section-subtitle,
  .photo-desc{margin-left:0}
  .country-heading{align-items:flex-start}
}
</style>

<script src="{{ '/assets/js/glightbox.min.js' | relative_url }}"></script>
<script>
window.addEventListener("load", ()=>{
  const nav=document.getElementById("gallery-nav");
  const sections=[...document.querySelectorAll(".country-section")];

  sections.forEach(sec=>{
    const name=sec.dataset.country;
    const id=name.toLowerCase();
    sec.id=id;
    const a=document.createElement("a");
    a.href=`#${id}`;
    a.textContent=name;
    nav.appendChild(a);
  });

  const navLinks=[...document.querySelectorAll('#gallery-nav a')];
  const spy=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        navLinks.forEach(l=>l.classList.remove('active'));
        const c=document.querySelector(`#gallery-nav a[href="#${e.target.id}"]`);
        if(c)c.classList.add('active');
      }
    });
  },{threshold:0.3,rootMargin:"-20% 0px -60% 0px"});
  sections.forEach(sec=>spy.observe(sec));

  const goTop=document.getElementById("go-top");

  const onScroll=()=>{
    nav.classList.toggle("shadow",window.scrollY>60);
    goTop.classList.toggle("show",window.scrollY>420);
  };
  onScroll();
  window.addEventListener("scroll",onScroll);

  goTop.addEventListener("click",()=>window.scrollTo({top:0,behavior:"smooth"}));

  const input=document.getElementById("country-search");
  const noRes=document.getElementById("no-result");
  input.addEventListener("input",()=>{
    const val=input.value.trim().toLowerCase();
    let visible=0;
    sections.forEach(sec=>{
      const match=sec.textContent.toLowerCase().includes(val);
      sec.style.display=match?"":"none";
      if(match)visible++;
    });
    noRes.style.display=(visible===0&&val!=="")?"block":"none";
  });

  const imgs=document.querySelectorAll(".gallery img");
  const io=new IntersectionObserver(es=>{
    es.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add("visible");
        io.unobserve(e.target);
      }
    });
  },{rootMargin:"0px 0px -10% 0px"});
  imgs.forEach(i=>io.observe(i));

  document.querySelectorAll(".country-header .toggle").forEach(h3=>{
    h3.addEventListener("click",()=>{
      const gal=h3.parentElement.parentElement.querySelector(".gallery");
      gal.style.display=(gal.style.display==='none'?'block':'none');
    });
  });

  let currentLang='en';
  const galleryLinks=[...document.querySelectorAll("a.glightbox")];

  function slidePath(url){
    try{return new URL(url,location.href).pathname;}
    catch(e){return url||"";}
  }

  galleryLinks.forEach(link=>{
    link.classList.remove("image-popup");
    link.setAttribute("data-description",buildCaption(link,currentLang));
  });

  const btn=document.createElement("button");
  btn.id="lang-toggle";
  btn.textContent="EN / 中文";
  btn.addEventListener("click",()=>{
    currentLang=(currentLang==='en'?'zh':'en');
    updateLang();
  });
  document.body.appendChild(btn);

  function findGalleryLink(src){
    const path=slidePath(src);
    return galleryLinks.find(link=>slidePath(link.getAttribute("href"))===path);
  }

  function buildCaption(link,lang){
    if(!link)return"";
    const isZh=lang==='zh';
    const title=link.getAttribute("data-title")||"";
    const date=link.dataset.captionDate||"";
    const location=isZh?(link.dataset.captionLocationZh||link.dataset.captionLocationEn||""):(link.dataset.captionLocationEn||"");
    const place=isZh?(link.dataset.captionPlaceZh||link.dataset.captionPlaceEn||""):(link.dataset.captionPlaceEn||"");
    const desc=isZh?(link.dataset.captionDescZh||link.dataset.captionDescEn||""):(link.dataset.captionDescEn||"");
    const labels=isZh
      ?{date:"时间",location:"地点",place:"地点 / 背景"}
      :{date:"Date",location:"Location",place:"Place / Background"};

    return `
      <div class="caption-panel">
        <div class="caption-panel__title">${title}</div>
        <div class="caption-panel__meta">
          <span class="caption-panel__meta-item"><strong>${labels.date}:</strong> ${date}</span>
          <span class="caption-panel__meta-item"><strong>${labels.location}:</strong> ${location}</span>
          <span class="caption-panel__meta-item"><strong>${labels.place}:</strong> ${place}</span>
        </div>
        ${desc?`<p class="caption-panel__text">${desc}</p>`:""}
      </div>
    `;
  }

  function updateLang(){
    document.querySelectorAll(".gslide-description .gdesc-inner").forEach(el=>{
      const slide=el.closest(".gslide");
      const img=slide?.querySelector(".gslide-image img");
      if(!img)return;
      const src=img.getAttribute("src")||img.getAttribute("data-src")||"";
      const link=findGalleryLink(src);
      el.innerHTML=buildCaption(link,currentLang);
    });
  }

  GLightbox({
    selector:".glightbox",
    touchNavigation:true,
    loop:true,
    zoomable:true,
    descPosition:"bottom",
    onOpen:()=>setTimeout(updateLang,0),
    afterSlideChange:()=>updateLang()
  });
});
</script>
