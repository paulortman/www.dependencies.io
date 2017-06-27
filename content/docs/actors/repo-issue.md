---
date: 2017-06-16T14:50:23.362599
draft: false
title: "Actor: repo-issue"
---

[![dependencies.io](https://img.shields.io/badge/dependencies.io-actor-3DA4E9.svg)](https://www.dependencies.io/docs/actors/)
[![Docker](https://img.shields.io/badge/dockerhub-actor--repo--issue-22B8EB.svg)](https://hub.docker.com/r/dependencies/actor-repo-issue/)
[![GitHub release](https://img.shields.io/github/release/dependencies-io/actor-repo-issue.svg)](https://github.com/dependencies-io/actor-repo-issue/releases)
[![Build Status](https://travis-ci.org/dependencies-io/actor-repo-issue.svg?branch=master)](https://travis-ci.org/dependencies-io/actor-repo-issue)
[![license](https://img.shields.io/github/license/dependencies-io/actor-repo-issue.svg)](https://github.com/dependencies-io/actor-repo-issue/blob/master/LICENSE)

A [dependencies.io](https://www.dependencies.io)
[actor](https://www.dependencies.io/docs/actors/) creates GitHub issues to notify
you of new versions.

## Usage

For each dependency, it will create 1 issue and list out all of the new versions
that are available for it and any additional information about them.

### .dependencies.yml

```yaml
collectors:
- ...
  actors:
  - type: repo-issue
    versions: "L.Y.Y"
    settings:  # all settings are optional
      issue_labels:  # list of label names
      - bug
      issue_assignees:  # list of usernames
      - davegaeddert
      issue_milestone: 3  # milestone number
```

### Works well with

- [python-pip collector](https://www.dependencies.io/docs/collectors/python-pip/) ([GitHub repo](https://github.com/dependencies-io/collector-python-pip/))
- [js-npm collector](https://www.dependencies.io/docs/collectors/js-npm/) ([GitHub repo](https://github.com/dependencies-io/collector-js-npm/))
- [git-repo collector](https://www.dependencies.io/docs/collectors/git-repo/) ([GitHub repo](https://github.com/dependencies-io/collector-git-repo/))


## Resources

- https://developer.github.com/v3/issues/#create-an-issue

## Support

Any questions or issues with this specific actor should be discussed in [GitHub
issues](https://github.com/dependencies-io/actor-repo-issue/issues). If there is
private information which needs to be shared then you can instead use the
[dependencies.io support](https://app.dependencies.io/support).
