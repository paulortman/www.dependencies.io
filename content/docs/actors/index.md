---
date: 2017-05-11T11:10:48-05:00
draft: false
title: Actors
---

Actors take a list of dependencies and the versions available, and perform some
action. For some dependencies (or specific versions), you might just want a
light notification -- GitHub issues and Slack are perfect for that. For others,
you might want to have a pull request created for you.

### Official generic actors

- [repo-issue](repo-issue)
- [find-replace](find-replace)

### Official language-specific actors

- [python-pip](python-pip)
- [js-npm](js-npm)

## dependencies.yml

Only two fields are required for each actor: `type`, `versions`

```yaml
- type: python-pip  # one of the official actors

  # filter the versions that this actor will act on (i.e. only minor and patches, etc.)
  versions: "L.Y.Y"

  # a regex for filtering based on dependency name (matches all by default)
  dependencies: ".*"

  # some actors have optional settings that you can use
  settings:
    pr_labels:
    - dependencies
```
