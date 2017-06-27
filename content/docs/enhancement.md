---
date: 2017-05-11T11:10:48-05:00
draft: false
title: Enhancement
---

For the more popular package management systems, we take things one step
further. Our proprietary (?) release enhancement service will take a given
dependency version, and go out to find all the information that we can, saving
you the work of tracking down exactly what each update is about and how it will
impact you.

The enhancement runs in between the collection and actions, so any additional
discovered information will be passed on to the actors and can provide more
details notifications than they could otherwise.

### What we can find

- source code repo (GitHub, GitLab)
- blog posts
- source code diffs between versions
- release notes not published via package manager

### Supported sources

- pypi
- npm
- github

The source is pulled from `package.source` as defined in the schema.
