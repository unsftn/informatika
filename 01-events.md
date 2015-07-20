---
layout: page
title: News & Events
permalink: /events/
---

{% for post in site.posts  %}
  {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}
  {% if forloop.first %}
  
### {{this_year}}
  
  {% endif %}
  - {{post.date | date: "%Y-%m-%d"}} [{{ post.title }}]({{ post.url }})
  {% if forloop.last == false %}
  {% if this_year != next_year %}
  
### {{next_year}}
  
  {% endif %}
  {% endif %}
{% endfor %}


