---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

Welcome to my personal website!

<p style="margin-bottom: 10px;">
Hi! I’m <strong>Zhi Chen</strong>, a first-year Ph.D. student in Supply Chain Management at the 
<strong>C. T. Bauer College of Business, University of Houston</strong>.
</p>

<p style="margin-bottom: 10px;">
My research interests focus on <em>Healthcare Operations</em>, <em>Digital Platforms</em>, <em>Retail Operations</em>, 
<em>Online Reviews</em>, and <em>Information Technology</em>.
</p>

<p style="margin-bottom: 10px;">
In my leisure time, I enjoy traveling, exploring cities, experiencing diverse cultures, 
and playing sports such as basketball, badminton, and cycling.
</p>

<hr style="margin-top: 25px; margin-bottom: 20px;">

<!-- ========= News + Visitors Map Section ========= -->
<div style="background-color: #f6f7f8; padding: 25px; border-radius: 10px; margin-top: 30px;">
  <h2 style="margin-top: 0; margin-bottom: 20px;">📰 News & 🌍 Visitors Map</h2>

  <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start; gap: 30px;">

    <!-- Left Column: News -->
    <div style="flex: 1 1 48%; min-width: 300px;">
      <h3 style="border-bottom: 2px solid #ccc; padding-bottom: 4px; margin-bottom: 12px;">News</h3>

      <!-- Year 2025 -->
      <h4 style="color:#004c97; margin-bottom: 10px; margin-top: 20px;">2025</h4>
      <ul style="list-style: none; padding-left: 15px; border-left: 3px solid #007acc; line-height: 1.8;">
        <li style="margin-bottom: 14px; position: relative;">
          <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
          <strong>Oct:</strong> Presented at the <em>INFORMS Annual Meeting</em> in Atlanta.
        </li>
        <li style="margin-bottom: 14px; position: relative;">
          <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
          <strong>Sep:</strong> Paper under review at <em>Manufacturing & Service Operations Management</em>.
        </li>
        <li style="margin-bottom: 14px; position: relative;">
          <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
          <strong>Aug:</strong> Joined the Ph.D. program at the University of Houston.
        </li>
      </ul>

      <!-- Year 2024 -->
      <h4 style="color:#004c97; margin-bottom: 10px; margin-top: 25px;">2024</h4>
      <ul style="list-style: none; padding-left: 15px; border-left: 3px solid #007acc; line-height: 1.8;">
        <li style="margin-bottom: 14px; position: relative;">
          <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
          <strong>Dec:</strong> Completed my M.S. in Supply Chain Management at Tongji University.
        </li>
        <li style="margin-bottom: 14px; position: relative;">
          <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
          <strong>Nov:</strong> Presented research on platform operations at the <em>Chinese Academy of Management Annual Meeting</em>.
        </li>
      </ul>

      <!-- Older News (collapsible section) -->
      <div id="old-news" style="display: none;">
        <h4 style="color:#004c97; margin-bottom: 10px; margin-top: 25px;">2023</h4>
        <ul style="list-style: none; padding-left: 15px; border-left: 3px solid #007acc; line-height: 1.8;">
          <li style="margin-bottom: 14px; position: relative;">
            <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
            <strong>Oct:</strong> Co-authored a working paper on behavioral operations.
          </li>
          <li style="margin-bottom: 14px; position: relative;">
            <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
            <strong>May:</strong> Presented a student paper at the <em>Tongji University Research Forum</em>.
          </li>
        </ul>

        <h4 style="color:#004c97; margin-bottom: 10px; margin-top: 25px;">2022</h4>
        <ul style="list-style: none; padding-left: 15px; border-left: 3px solid #007acc; line-height: 1.8;">
          <li style="margin-bottom: 14px; position: relative;">
            <span style="position: absolute; left: -10px; top: 8px; width: 10px; height: 10px; background-color: #007acc; border-radius: 50%;"></span>
            <strong>Dec:</strong> Began research on digital marketplace competition.
          </li>
        </ul>
      </div>

      <!-- Show/Hide Button -->
      <div style="text-align:center; margin-top:10px;">
        <button onclick="toggleNews()" id="toggleButton"
          style="background-color:#004c97; color:white; border:none; border-radius:6px; padding:6px 14px; cursor:pointer; font-size:0.9em;">
          Show More ⬇️
        </button>
      </div>

      <script>
        function toggleNews() {
          var oldNews = document.getElementById('old-news');
          var btn = document.getElementById('toggleButton');
          if (oldNews.style.display === 'none') {
            oldNews.style.display = 'block';
            btn.textContent = 'Show Less ⬆️';
          } else {
            oldNews.style.display = 'none';
            btn.textContent = 'Show More ⬇️';
          }
        }
      </script>
    </div>

    <!-- Right Column: Visitors Map -->
    <div style="flex: 1 1 48%; min-width: 300px;">
      <h3 style="border-bottom: 2px solid #ccc; padding-bottom: 4px; margin-bottom: 12px;">Visitors Map</h3>
      <div style="text-align: center;">
        <script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=oPLM1fsDm01h0b7IlUIRdDxjeBc3a5aCKYY4XINKs1g&cl=ffffff&w=a"></script>
        <p style="font-size: 0.9em; color: #666; margin-top: 8px;">Tracking visitors since October 2025</p>
      </div>
    </div>
  </div>
</div>
