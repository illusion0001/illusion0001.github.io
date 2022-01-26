---
layout: page
title: "The Last of Us"
excerpt: My modifications and patches for The Last of Us games.
image: "https://storage.googleapis.com/assets-illusion0001/images/portf/t1/t1-logo.png"
feature-img: "https://storage.googleapis.com/assets-illusion0001/images/portf/t1/t1-logo.png"
game-series: "tlou"
order: -100
---

{% assign items = site.games | where:"parent-series", page.game-series %}
{% include mods-grid.html items=items cell-size="33%" %}
