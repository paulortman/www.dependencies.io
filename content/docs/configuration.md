---
date: 2017-05-11T11:10:48-05:00
draft: false
title: Configuration
---

A `dependencies.yml` file at the root of your repo tells us what you want
to happen. For each dependency file you have, you'll add a [collector]({{< relref
"docs/collectors/index.md" >}}). To each collector you then add [actors]({{< relref
"docs/actors/index.md" >}}) to decide what you want to happen when
[new versions]({{< relref "docs/dependencies-yml/version-filtering.md" >}})
are found.

```yaml
collectors:

- type: python-pip  # name of an official collector
  path: requirements.txt  # which file the collector should read
  actors:
  - type: python-pip  # name of an official actor
    dependencies: ".*"  # regular expression for filtering dependencies by name
    versions: "L.Y.Y"  # versions that this actor should act on
    settings:  # settings for this specific actor
      pr_labels:
      - dependencies

- type: js-npm
  path: app  # the js-npm collector is given directories (which could have package.json, yarn.lock, etc.)
  actors:
  - type: js-npm
    dependencies: "react-.*"
    versions: "L.Y.Y"
  - type: repo-issue
    dependencies: "react-.*"
    versions: "Y.0.0"

```
