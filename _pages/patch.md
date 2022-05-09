---
layout: single
title: Patches
permalink: /patch/
---

[Installation Guide](/install-instructions/)

This site lists patches made for use with exploited consoles.

# Sponsors and Social Links

- Support on [Buy me a Coffee](https://www.buymeacoffee.com/illusion0001)
- Support on [GitHub Sponsors](https://github.com/sponsors/illusion0001)
- Support on [Ko-fi](https://ko-fi.com/illusion0001)
- Support on [Patreon](https://www.patreon.com/illusion0001)
- Follow on [YouTube](https://youtube.com/c/illusion0001)
- Follow on [Twitter](https://twitter.com/illusion0002)

# Contributing

You can submit a pull request to this [repository](https://github.com/illusion0001/illusion0001.github.io/tree/main/_patch0) with your own patches.

YML syntax example: [example.yml](https://github.com/illusion0001/py-patcher/blob/137529109cdd58e2b977162e09bdad8849df5301/data/example.yml#L26-L54)

## Patches

{% for _patch in site._patch %}
- [{{ _patch.title }}]({{ _patch.url }})
{% endfor %}
