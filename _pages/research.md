---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% if site.author.googlescholar %}
<div class="wordwrap">
  You can also find my articles on
  <a href="{{ site.author.googlescholar }}" target="_blank">my Google Scholar profile</a>.
</div>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<p style="text-align:center; font-size:1.1em; margin-top:40px; color:#777;">
  Research section under update.
</p>
