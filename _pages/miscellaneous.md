---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<h1 id="top" class="tg-page-title">🌍 Travel Gallery</h1>
<p class="tg-page-subtitle">Every journey tells a story — automatically organized by year, country, and light.</p>

<nav id="gallery-nav"></nav>
<div class="timeline"></div>
<div id="gallery-container"></div>

<hr style="margin-top:60px; margin-bottom:10px;">
<p style="text-align:center;">
  <b>Email:</b> <a href="mailto:zhichen.colin@gmail.com">zhichen.colin@gmail.com</a>
</p>

<link rel="stylesheet" href="{{ '/assets/css/glightbox.min.css' | relative_url }}">
<style>
:root {
  --tg-accent:#4a7bd0;
  --tg-text:#333;
  --tg-muted:#666;
}
@media(prefers-color-scheme:dark){
  :root{ --tg-text:#eee; --tg-muted:#aaa; --tg-accent:#81aef7; background:#111; color:#eee;}
}
.tg-page-title{text-align:center;font-size:28px;}
.tg-page-subtitle{text-align:center;font-size:16px;color:var(--tg-muted);margin-bottom:30px;}
#gallery-nav{position:sticky;top:0;z-index:99;background:rgba(255,255,255,.96);backdrop-filter:blur(6px);text-align:center;padding:10px;border-bottom:1px solid #ddd;}
#gallery-nav a{margin:0 6px;padding:8px 14px;border-radius:999px;background:#f4f4f4;text-decoration:none;color:#333;font-weight:600;transition:.3s;}
#gallery-nav a.active,#gallery-nav a:hover{background:linear-gradient(135deg,var(--tg-accent),#333);color:#fff;}
.timeline{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;font-size:14px;color:var(--tg-muted);margin-bottom:25px;}
.timeline span{background:#f9f9f9;padding:6px 12px;border-radius:8px;}
.year-block{margin-bottom:80px;padding:20px;border-radius:18px;background:linear-gradient(180deg,#f9fbff,#fff);box-shadow:0 2px 10px rgba(0,0,0,0.05);}
.year-header{cursor:pointer;text-align:center;font-size:22px;font-weight:700;margin-bottom:15px;padding:10px;border-bottom:1px solid #ddd;transition:.3s;}
.year-header:hover{color:var(--tg-accent);}
.year-content{display:none;animation:fadeIn .5s ease;}
.country-section{background:linear-gradient(180deg,var(--theme2) 0%,#fff 100%);border-radius:14px;padding:25px 20px;margin-bottom:50px;box-shadow:0 2px 10px rgba(0,0,0,0.05);}
.country-header h3{color:var(--theme1);font-size:20px;font-weight:700;}
.country-header p{color:var(--tg-muted);font-size:15px;}
.gallery{column-count:3;column-gap:15px;}
.gallery a{display:inline-block;}
.gallery img{width:100%;border-radius:10px;margin-bottom:15px;break-inside:avoid;opacity:0;transform:translateY(10px);transition:.8s;}
.gallery img.visible{opacity:1;transform:translateY(0);}
.gallery img:hover{transform:scale(1.02);box-shadow:0 8px 16px rgba(0,0,0,.15);}
#tg-backtop{position:fixed;right:22px;bottom:26px;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;background:linear-gradient(135deg,var(--tg-accent),#111);box-shadow:0 8px 22px rgba(0,0,0,.22);opacity:0;visibility:hidden;transition:.4s;animation:breath 2s infinite;}
#tg-backtop.show{opacity:1;visibility:visible;}
#tg-backtop:hover{transform:translateY(-3px);}
#tg-backtop .tooltip{position:absolute;right:60px;bottom:10px;background:#111;color:#fff;padding:5px 8px;border-radius:6px;font-size:12px;opacity:0;transition:.2s;}
#tg-backtop:hover .tooltip{opacity:1;}
@keyframes breath{0%,100%{box-shadow:0 0 12px rgba(74,123,208,.6);}50%{box-shadow:0 0 20px rgba(74,123,208,.8);}}
@keyframes fadeIn{from{opacity:0;}to{opacity:1;}}
@media(max-width:1000px){.gallery{column-count:2;}}@media(max-width:700px){.gallery{column-count:1;}}
</style>

<script src="{{ '/assets/js/glightbox.min.js' | relative_url }}"></script>
<script>
document.addEventListener("DOMContentLoaded",()=>{
  const galleryContainer=document.getElementById("gallery-container");

  // 自动扫描年份、月份、国家（伪扫描逻辑，可手动扩展后台索引）
  const years=["2023","2022"];
  const countriesPerYear={
    "2023":["jan_sweden"],
    "2022":["nov_denmark","oct_italy","sep_france","aug_germany"]
  };

  // 自动生成年份分区
  years.forEach(year=>{
    const yearBlock=document.createElement("div");
    yearBlock.className="year-block";
    const header=document.createElement("div");
    header.className="year-header";
    header.textContent=year+" ✦";
    const content=document.createElement("div");
    content.className="year-content";
    header.addEventListener("click",()=>{content.style.display=(content.style.display==="block")?"none":"block";});
    yearBlock.append(header,content);
    galleryContainer.appendChild(yearBlock);

    // 每个国家生成区块
    countriesPerYear[year].forEach(folder=>{
      const [mon,countryRaw]=folder.split("_");
      const country=countryRaw.charAt(0).toUpperCase()+countryRaw.slice(1);
      const color1=randomColor();
      const color2=tintColor(color1,80);
      const section=document.createElement("div");
      section.className="country-section";
      section.dataset.country=country;
      section.style=`--theme1:${color1};--theme2:${color2}`;
      section.id=country.toLowerCase();
      section.innerHTML=`
        <div class="country-header">
          <h3>${mon.charAt(0).toUpperCase()+mon.slice(1)}. ${year} – ${country}</h3>
          <p>${country} travel memories — light, rhythm, and calm.</p>
        </div>
        <div class="gallery" id="gallery-${country.toLowerCase()}"></div>
        <div class="back-top-inline"><a href="#top">↑ Back to Top</a></div>`;
      content.appendChild(section);

      // 自动加载图片 (最多40张)
      const g=document.getElementById(`gallery-${country.toLowerCase()}`);
      for(let i=1;i<=40;i++){
        const path=`{{ site.baseurl }}/images/travel/${year}/${folder}/${year}_${country.toLowerCase()}_${i}.jpg`;
        const a=document.createElement("a");
        a.href=path;
        a.className="glightbox";
        a.dataset.gallery=country.toLowerCase();
        a.dataset.title=formatTitle(path);
        const img=document.createElement("img");
        img.src=path;
        img.alt=country+" photo "+i;
        a.appendChild(img);
        g.appendChild(a);
      }
    });
  });

  // 自动导航栏 + 时间轴
  const nav=document.getElementById("gallery-nav");
  const timeline=document.querySelector(".timeline");
  years.forEach(y=>{
    const link=document.createElement("a");
    link.href="#"+y;
    link.textContent=y;
    nav.appendChild(link);
    const t=document.createElement("span");
    t.textContent=y;
    timeline.appendChild(t);
  });

  // 动画
  const imgs=document.querySelectorAll(".gallery img");
  const fadeIn=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add("visible");fadeIn.unobserve(e.target);}});
  });
  imgs.forEach(img=>fadeIn.observe(img));

  // 返回顶部按钮
  const back=document.createElement("div");
  back.id="tg-backtop";
  back.innerHTML="↑<span class='tooltip'>Back to Top</span>";
  document.body.appendChild(back);
  window.addEventListener("scroll",()=>{if(window.scrollY>600)back.classList.add("show");else back.classList.remove("show");});
  back.addEventListener("click",()=>window.scrollTo({top:0,behavior:"smooth"}));

  // Lightbox
  GLightbox({selector:".glightbox",loop:true,openEffect:"zoom",closeEffect:"fade"});

  // 工具函数
  function formatTitle(src){
    const name=src.split("/").pop().split(".")[0].replace(/_/g," ");
    return name.split(" ").map(w=>w.charAt(0).toUpperCase()+w.slice(1)).join(" ");
  }
  function randomColor(){
    const colors=["#3498db","#9b59b6","#16a085","#e67e22","#c0392b","#1abc9c","#2ecc71","#f39c12"];
    return colors[Math.floor(Math.random()*colors.length)];
  }
  function tintColor(hex,percent){
    const num=parseInt(hex.slice(1),16),
      amt=Math.round(2.55*percent),
      R=(num>>16)+amt,G=(num>>8&0x00FF)+amt,B=(num&0x0000FF)+amt;
    return "#"+(0x1000000+
      (R<255?R<1?0:R:255)*0x10000+
      (G<255?G<1?0:G:255)*0x100+
      (B<255?B<1?0:B:255))
      .toString(16).slice(1);
  }
});
</script>
