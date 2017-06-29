---
date: 2017-05-11T11:10:48-05:00
draft: false
title: Introduction
---

Dependencies.io is a hosted service for managing project dependencies. Once
installed on your git repo, we will collect the various dependency versions that
you use and identify which have updates available. With that information we can
keep you informed and even automate your dependency updates. The platform is
designed to be flexible with your workflow, and can do anything from send your
team a Slack message, to create a GitHub pull request with the update already
made.

All it requires is a single `dependencies.yml` file at the root of your repo,
which points us to the various dependency files in your project. Depending on
the type of dependencies in each file, we'll run a [collector]({{< relref
"docs/collectors/index.md" >}}) to find out what you have installed and which
versions are available, then any [actors]({{< relref
"docs/actors/index.md" >}}) to deliver those updates to you.

## How is this different from other services?

As you'd expect, there are a handful of other services and tools out there that
can help you stay on top of dependencies. Most of them are language specific,
and only support certain setups or configurations. Everyone develops software a
little bit differently. It's not uncommon for a single project to use several
different languages, frameworks, and package management tools.

By leveraging [docker containers](https://www.docker.com/what-container), we set out to build a single service that
could work with anything that you do. You shouldn't have to use multiple
services to automate your dependency management.

![Docker]({{< hash_img "docs/docker.png" >}})
