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

The list of courses

Civil Engineering
=================

The list of courses

Biomedical Engineering
======================

The list of courses

Geodesy and Geomatics
=====================

The list of courses