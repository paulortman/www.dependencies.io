---
date: 2017-06-29T15:47:28.434841
draft: false
title: "Actor: php-composer"
---


[![dependencies.io](https://img.shields.io/badge/dependencies.io-actor-3DA4E9.svg)](https://www.dependencies.io/docs/actors/)
[![Docker](https://img.shields.io/badge/dockerhub-actor--php--composer-22B8EB.svg)](https://hub.docker.com/r/dependencies/actor-php-composer/)
[![GitHub release](https://img.shields.io/github/release/dependencies-io/actor-php-composer.svg)](https://github.com/dependencies-io/actor-php-composer/releases)
[![Build Status](https://travis-ci.org/dependencies-io/actor-php-composer.svg?branch=master)](https://travis-ci.org/dependencies-io/actor-php-composer)
[![license](https://img.shields.io/github/license/dependencies-io/actor-php-composer.svg)](https://github.com/dependencies-io/actor-php-composer/blob/master/LICENSE)

A [dependencies.io](https://www.dependencies.io)
[actor](https://www.dependencies.io/docs/actors/) that uses
`composer require $name:$version` to update composer dependencies.

## Usage

### .dependencies.yml

```yaml
collectors:
- ...
  actors:
  - type: php-composer
    versions: "L.Y.Y"
    settings:  # all settings are optional
      pr_labels:  # list of label names
      - bug
      pr_assignees:  # list of usernames
      - davegaeddert
      pr_milestone: 3  # milestone number
```

### Works well with

- [php-composer collector](https://www.dependencies.io/docs/collectors/php-composer/) ([GitHub repo](https://github.com/dependencies-io/collector-php-composer/))


## Resources

- https://getcomposer.org/doc/03-cli.md#require

## Support

Any questions or issues with this specific actor should be discussed in [GitHub
issues](https://github.com/dependencies-io/actor-php-composer/issues). If there is
private information which needs to be shared then you can instead use the
[dependencies.io support](https://app.dependencies.io/support).
