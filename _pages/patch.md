---
layout: post
title: Patches
permalink: /patch/
---

[Installation Guide](/install-instructions/)

This site lists patches made for use with exploited consoles.

{% include_relative _soical_links.md %}

# Contributing

You can submit a pull request to this [repository](https://github.com/illusion0001/PS4-PS5-Game-Patch) with your own patches.

## Patches

{% for _patch in site._patch %}
- [{{ _patch.title }}]({{ _patch.url }})
{% endfor %}
