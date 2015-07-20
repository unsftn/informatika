---
layout: page
title: Faculty
permalink: /faculty/
---

### Full Professors

{% for fac in site.faculty %}
  {% if fac.zvanje == "full" %}
  [{{fac.title}}]({{site.baseurl}}{{fac.url}})
  {% endif %}

{% endfor %}

### Associate Professors

{% for fac in site.faculty %}
  {% if fac.zvanje == "associate" %}
  [{{fac.title}}]({{site.baseurl}}{{fac.url}})
  {% endif %}

{% endfor %}

### Assistant Professors

{% for fac in site.faculty %}
  {% if fac.zvanje == "assistant" %}
  [{{fac.title}}]({{site.baseurl}}{{fac.url}})
  {% endif %}

{% endfor %}

### Lecturers

{% for fac in site.faculty %}
  {% if fac.zvanje == "lecturer" %}
  [{{fac.title}}]({{site.baseurl}}{{fac.url}})
  {% endif %}

{% endfor %}

### Teaching Assistants

{% for fac in site.faculty %}
  {% if fac.zvanje == "TA" %}
  [{{fac.title}}]({{site.baseurl}}{{fac.url}})
  {% endif %}

{% endfor %}

### Staff

{% for fac in site.faculty %}
  {% if fac.zvanje == "staff" %}
  [{{fac.title}}]({{site.baseurl}}{{fac.url}})
  {% endif %}

{% endfor %}

