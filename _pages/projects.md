---
layout: archive
permalink: /projects/
title: projects
author_profile: false
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
