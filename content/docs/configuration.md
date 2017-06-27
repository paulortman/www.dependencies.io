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
  - type: python-pip-github-pr  # name of an official actor
    packages: ".*"  # regular expression for filtering dependencies by name
    versions: Y.Y.Y  # versions that this actor should act on
    settings:  # settings for this specific actor
      pr_labels:
      - dependencies

- type: node-yarn
  path: react/package.json
  actors:
  - type: github-issue
    packages: "react-.*"
    versions: Y.N.N

```
