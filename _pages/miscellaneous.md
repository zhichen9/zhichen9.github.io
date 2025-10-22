---
layout: archive
title: ""
permalink: /miscellaneous/
author_profile: true
---

<h2>Travel Gallery</h2>

<p style="font-size: 16px; margin-bottom: 25px;">
This page collects some of my travel memories over the years, capturing moments from different cities and countries I have visited.
</p>

<!-- ===================
   🚫 以下部分暂时隐藏，保留以后用
=================== -->

<!--
<h3>Jan. 2023 – Sweden Memories</h3>
<div class="gallery">
  <img src="{{ site.baseurl }}/images/travel/2023_sweden1.jpg">
  <img src="{{ site.baseurl }}/images/travel/2023_sweden2.jpg">
</div>

<h3>Dec. 2022 – Denmark Memories</h3>
<div class="gallery">
  <img src="{{ site.baseurl }}/images/travel/2022_denmark1.jpg">
  <img src="{{ site.baseurl }}/images/travel/2022_denmark2.jpg">
</div>

<h3>Nov. 2022 – Italy Memories</h3>
<div class="gallery">
  <img src="{{ site.baseurl }}/images/travel/2022_italy1.jpg">
  <img src="{{ site.baseurl }}/images/travel/2022_italy2.jpg">
</div>

<h3>Oct. 2022 – France Memories</h3>
<div class="gallery">
  <img src="{{ site.baseurl }}/images/travel/2022_france1.jpg">
  <img src="{{ site.baseurl }}/images/travel/2022_france2.jpg">
</div>

<h3>Sep. 2022 – Sweden Memories</h3>
<div class="gallery">
  <img src="{{ site.baseurl }}/images/travel/2022_sweden1.jpg">
  <img src="{{ site.baseurl }}/images/travel/2022_sweden2.jpg">
</div>
-->



<!-- ===================
   ✅ 只显示德国部分
=================== -->

<h3>Aug. 2022 – Germany Memories</h3>
<div class="gallery">
  {% for i in (1..36) %}
    <img src="{{ site.baseurl }}/images/travel/2022/aug_germany/2022_germany_{{ i }}.jpg" width="250" style="margin:5px; border-radius:8px;">
  {% endfor %}
</div>

<hr style="margin-top:40px; margin-bottom:10px;">
<p>
<b>Email:</b> <a href="mailto:zhichen.colin@gmail.com">zhichen.colin@gmail.com</a>
</p>

<style>
.gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
  gap: 10px;
  margin-bottom: 30px;
}
.gallery img {
  width: 30%;
  max-width: 250px;
  height: auto;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.gallery img:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
</style>
