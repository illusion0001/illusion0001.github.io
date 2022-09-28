---
layout: single
title: Patches
permalink: /patch/
---

[Installation Guide](/install-instructions/)

This site lists patches made for use with exploited consoles.

{% include_relative _soical_links.md %}

# Contributing

You can submit a pull request to this [repository](https://github.com/illusion0001/console-game-patches) with your own patches.

YML syntax example: [example.yml](https://github.com/illusion0001/py-patcher/blob/137529109cdd58e2b977162e09bdad8849df5301/data/example.yml#L26-L54)

## Patches

{% for _patch in site._patch %}
- [{{ _patch.title }}]({{ _patch.url }})
{% endfor %}
