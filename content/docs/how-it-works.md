---
date: 2017-05-11T11:10:48-05:00
draft: false
title: How it works
---

Once a day we will automatically start a new "build" to check your dependencies.
A build is a 3-step process, defined by your `dependencies.yml` file.

#### 1) Collect

First we run a set of [collectors]({{< relref
"docs/collectors/index.md" >}}), which are language-specific docker containers
that use the native tools to detect what you have installed and what updates are
available.

A basic collector for javascript dependencies:

```yaml
collectors:
- type: js-npm
  path: /
  ...
```

#### 2) Version content discovery

Once we know what versions you want to be notified about, we run those through a
proprietary set of tools to go out and find as much information about each
release as we can. Packages don't always publish release notes in the same way,
and there is often a lot of additional information that isn't available through
the package management tools. We'll go out and look for blog posts, the
GitHub/GitLab/BitBucket repo, and other changelog systems to create the most
informative notifications that we can. This means that the notifications you get
from dependencies.io will be much more helpful than, _"Updates react to 15.0.0"_.

#### 3) Act

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
collectors:
- type: js-npm
  path: path/to/app
  actors:
  # create pull requests for patch updates
  - actor: js-npm
    dependencies: ".*"
    versions: "L.L.Y"
  # github issues to tell us about major and minor updates to our version
  - actor: repo-issue
    dependencies: ".*"
    versions: "Y.0.0 || L.Y.0"

- type: python-pip
  path: path/to/requirements.txt
  actors:
  # pull requests for patches to django packages
  - actor: repo-issue
    dependencies: "django-.*"
    versions: "L.L.Y"
```

<div class="window-frame"><img src="{{< hash_img "docs/pr-screenshot.png" >}}" alt="PR screenshot" /></div>

<small><em>(an example PR with additional content)</em></small>

---

### Open-source

All of our collectors and actors are open-source. We also allow qualified users
to run custom docker containers on dependencies.io -- which means if you want to
change how a collector or actor works, or even build your own from scratch, you
can. If you make something that other people could benefit from, let us know and
contribute it back to the community!

{{< btn url="https://github.com/dependencies-io" inner="Browse our repos" >}}
