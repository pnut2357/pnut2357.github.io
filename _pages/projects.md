---
layout: archive
permalink: /projects/
title: Projects
author_profile: true
#sidebar:
#  - image: "/assets/images/only-human-cover.jpg"
description: "test"
#og_image: "/assets/images/only-human-cover.jpg"
---
test

## Latest Stories

<div class="grid__wrapper">
  {% assign collection = 'projects' %}
  {% assign posts = site[collection] | reverse %}
  {% for post in posts %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
