---
date: 2017-05-11T11:10:48-05:00
draft: false
title: How it works
---

Once a day we will automatically start a new "build" to check your dependencies.
A build is a 3-step process, defined by your `dependencies.yml` file.

#### 1) [Collect]({{< relref "docs/collectors/index.md" >}})

First we run a set of [collectors]({{< relref
"docs/collectors/index.md" >}}), which are language-specific docker containers
that use the native tools to detect what you have installed and what updates are
available.

A basic collector for [node.js](#) dependencies:

```yaml
dependencies:
- collector: node-npm
  file: path/to/package.json
  ...
```

#### 2) [Enhance?]({{< relref "docs/enhancement.md" >}})

Once we know what versions you want to be notified about, we run those through a
proprietary set of tools to go out and find as much information about each
release as we can. Packages don't always publish release notes in the same way,
and there is often a lot of additional information that isn't available through
the package management tools. We'll go out and look for blog posts, the
GitHub/GitLab/BitBucket repo, and other changelog systems to create the most
informative notifications that we can. This means, especially for popular
packages, that the notifications you get from dependencies.io will be much more
helpful than, "Updates react to 15.0.0".

(screenshot of enhanced PR or issue)

#### 3) [Act]({{< relref "docs/actors/index.md" >}})

Once we have a list of your current and available dependency versions, we can
automate the tedious work of keeping you informed and your packages up-to-date.
You can choose any [actors]({{< relref "docs/actors/index.md" >}}) that fit your
workflow. For major versions you might just want a notification it was released
(Slack, GitHub issue, email, etc.). For minor and patch updates, you might want
an actor to actually install the update and create a pull request for you to
review. Actors are also just docker containers, so the only limitation is your
imagination. 😉

For each collector, you attach a set of actors to handle the updates.

```yaml
dependencies:
- collector: node-npm
  file: path/to/package.json
  actors:
  # create pull requests for patch updates
  - actor: node-npm-github-pr
    packages: ".*"
    versions: "L.L.Y"
  # github issues to tell us about major and minor updates to our version
  - actor: github-issue
    packages: ".*"
    versions: "Y.N.N || L.Y.N"

- collector: python-pip
  file: path/to/requirements.txt
  actors:
  # pull requests for patches to django packages
  - actor: github-issue
    packages: "django-.*"
    versions: "L.L.Y"
```

{{< btn url="#" inner="Look at example use cases" >}}

### Open-source

All of our collectors and actors are open-source. We also allow qualified users
to run custom docker containers on dependencies.io -- which means if you want to
change how a collector or actor works, or even build your own from scratch, you
can. If you make something that other people could benefit from, let us know and
contribute it back to the community!
