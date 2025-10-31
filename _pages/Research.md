---
layout: archive
title: "Research"
permalink: /Research/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% comment %}
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
{% endcomment %}

<p style="text-align:center; font-size:1.2em; margin-top:50px;">
  Research section under update.
</p>
