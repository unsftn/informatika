---
layout: page
title: Courses
permalink: /courses/
---

The courses taught by our faculty are listed by the curriculum.

Software Engineering and Information Technologies
=================================================

{% for course in site.courses %}
  {% if course.curriculum contains "SIIT" %}
  [{{course.title}}]({{site.baseurl}}{{course.url}})
  {% endif %}

{% endfor %}

Computing and Control
=====================

{% for course in site.courses %}
  {% if course.curriculum contains "E2" %}
  [{{course.title}}]({{site.baseurl}}{{course.url}})
  {% endif %}
  
{% endfor %}

Graphical Engineering and Design
================================

{% for course in site.courses %}
  {% if course.curriculum contains "GRID" %}
  [{{course.title}}]({{site.baseurl}}{{course.url}})
  {% endif %}

{% endfor %}


Civil Engineering
=================

{% for course in site.courses %}
  {% if course.curriculum contains "GRAD" %}
  [{{course.title}}]({{site.baseurl}}{{course.url}})
  {% endif %}

{% endfor %}


Biomedical Engineering
======================

{% for course in site.courses %}
  {% if course.curriculum contains "BIOMED" %}
  [{{course.title}}]({{site.baseurl}}{{course.url}})
  {% endif %}

{% endfor %}


Geodesy and Geomatics
=====================

{% for course in site.courses %}
  {% if course.curriculum contains "GEO" %}
  [{{course.title}}]({{site.baseurl}}{{course.url}})
  {% endif %}

{% endfor %}
