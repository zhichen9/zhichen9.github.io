---
layout: archive
title: "Travel Gallery"
permalink: /miscellaneous/
author_profile: true
use_javascript: true
---

# 🌍 Travel Gallery
_A collection of travel memories — each place tells a story of moments, light, and time._

<div class="filter-container">
  <div id="year-filters" class="year-filters"></div>
  <div id="country-filters" class="country-filters"></div>
</div>
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
h1{text-align:center;margin-bottom:5px;}
.filter-container{text-align:center;margin:20px 0;}
.country-filters button, .year-filters button{
  margin:5px;
  padding:8px 16px;
  border:none;
  border-radius:20px;
  background:#f4f4f4;
  color:var(--tg-text);
  cursor:pointer;
  font-weight:600;
  transition:.3s;
}
.country-filters button.active, .year-filters button.active,
.country-filters button:hover, .year-filters button:hover{
  background:linear-gradient(135deg,var(--tg-accent),#333);
  color:#fff;
}
.year-filters{margin-bottom:15px;}
.gallery{column-count:3;column-gap:15px;}
.gallery a{display:inline-block;}
.gallery img{width:100%;border-radius:10px;margin-bottom:15px;break-inside:avoid;opacity:0;transform:translateY(10px);transition:.8s;}
.gallery img.visible{opacity:1;transform:translateY(0);}
.gallery img:hover{transform:scale(1.02);box-shadow:0 8px 16px rgba(0,0,0,.15);}
.country-section{background:linear-gradient(180deg,var(--theme2) 0%,#fff 100%);border-radius:14px;padding:25px 20px;margin-bottom:40px;box-shadow:0 2px 10px rgba(0,0,0,0.05);}
.country-header h3{color:var(--theme1);font-size:20px;font-weight:700;}
.country-header p{color:var(--tg-muted);font-size:15px;}
#tg-backtop{position:fixed;right:22px;bottom:26px;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;background:linear-gradient(135deg,var(--tg-accent),#111);box-shadow:0 8px 22px rgba(0,0,0,.22);opacity:0;visibility:hidden;transition:.4s;animation:breath 2s infinite;}
#tg-backtop.show{opacity:1;visibility:visible;}
#tg-backtop:hover{transform:translateY(-3px);}
#tg-backtop .tooltip{position:absolute;right:60px;bottom:10px;background:#111;color:#fff;padding:5px 8px;border-radius:6px;font-size:12px;opacity:0;transition:.2s;}
#tg-backtop:hover .tooltip{opacity:1;}
@keyframes breath{0%,100%{box-shadow:0 0 12px rgba(74,123,208,.6);}50%{box-shadow:0 0 20px rgba(74,123,208,.8);}}
@media(max-width:1000px){.gallery{column-count:2;}}@media(max-width:700px){.gallery{column-count:1;}}
</style>

<script src="{{ '/assets/js/glightbox.min.js' | relative_url }}"></script>
<script>
document.addEventListener("DOMContentLoaded",()=>{
  const galleryContainer=document.getElementById("gallery-container");

  // 🗓️ 年份与国家配置
  const years=["2023","2022"];
  const countriesPerYear={
    "2023":["jan_sweden"], // 可为空
    "2022":["nov_denmark","oct_italy","sep_france","aug_germany"]
  };

  // 🌍 国家筛选器
  const allCountries=["All","Denmark","Italy","France","Germany","Sweden"];
  const countryDiv=document.getElementById("country-filters");
  allCountries.forEach(c=>{
    const btn=document.createElement("button");
    btn.textContent=c;
    btn.dataset.country=c.toLowerCase();
    btn.addEventListener("click",()=>{
      document.querySelectorAll(".country-section").forEach(sec=>{
        if(c==="All"||sec.dataset.country===c.toLowerCase()) sec.style.display="block";
        else sec.style.display="none";
      });
      document.querySelectorAll(".country-filters button").forEach(b=>b.classList.remove("active"));
      btn.classList.add("active");
    });
    countryDiv.appendChild(btn);
  });

  // 📅 年份筛选器
  const yearDiv=document.getElementById("year-filters");
  years.forEach(y=>{
    const btn=document.createElement("button");
    btn.textContent=y;
    btn.dataset.year=y;
    btn.addEventListener("click",()=>{
      document.querySelectorAll(".year-block").forEach(block=>{
        if(block.dataset.year===y) block.style.display="block";
        else block.style.display="none";
      });
      document.querySelectorAll(".year-filters button").forEach(b=>b.classList.remove("active"));
      btn.classList.add("active");
    });
    yearDiv.appendChild(btn);
  });
  yearDiv.querySelector("button").classList.add("active");
  countryDiv.querySelector("button").classList.add("active");

  // 🔄 动态生成年份与图片内容
  years.forEach(year=>{
    const yearBlock=document.createElement("div");
    yearBlock.className="year-block";
    yearBlock.dataset.year=year;
    const content=document.createElement("div");
    yearBlock.append(content);
    galleryContainer.appendChild(yearBlock);

    countriesPerYear[year].forEach(folder=>{
      const [mon,countryRaw]=folder.split("_");
      const country=countryRaw.charAt(0).toUpperCase()+countryRaw.slice(1);
      const color1=randomColor();
      const color2=tintColor(color1,80);
      const section=document.createElement("div");
      section.className="country-section";
      section.dataset.country=country.toLowerCase();
      section.style=`--theme1:${color1};--theme2:${color2}`;
      section.id=country.toLowerCase();
      section.innerHTML=`
        <div class="country-header">
          <h3>${mon.charAt(0).toUpperCase()+mon.slice(1)}. ${year} – ${country} Memories</h3>
          <p>${country} travel moments — light, rhythm, and calm.</p>
        </div>
        <div class="gallery" id="gallery-${country.toLowerCase()}-${year}"></div>`;
      content.appendChild(section);

      // ♾️ 无限加载图片
      const g=document.getElementById(`gallery-${country.toLowerCase()}-${year}`);
      let index=1;
      const basePath="{{ site.baseurl }}" + `/images/travel/${year}/${folder}/`;
      const loadImage=()=>{
        const path=basePath+`${year}_${country.toLowerCase()}_${index}.jpg`;
        const img=new Image();
        img.onload=()=>{
          const a=document.createElement("a");
          a.href=path;
          a.className="glightbox";
          a.dataset.gallery=country.toLowerCase()+year;
          const im=document.createElement("img");
          im.src=path;
          im.alt=country+" photo "+index;
          a.appendChild(im);
          g.appendChild(a);
          fadeIn.observe(im);
          index++;
          loadImage();
        };
        img.onerror=()=>{};
        img.src=path;
      };
      loadImage();
    });
  });

  // 🪄 淡入动画
  const fadeIn=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add("visible");fadeIn.unobserve(e.target);}});
  });

  // 🔝 返回顶部
  const back=document.createElement("div");
  back.id="tg-backtop";
  back.innerHTML="↑<span class='tooltip'>Back to Top</span>";
  document.body.appendChild(back);
  window.addEventListener("scroll",()=>{if(window.scrollY>600)back.classList.add("show");else back.classList.remove("show");});
  back.addEventListener("click",()=>window.scrollTo({top:0,behavior:"smooth"}));

  // 💡 Lightbox
  GLightbox({selector:".glightbox",loop:true,openEffect:"zoom",closeEffect:"fade"});

  // 工具函数
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
