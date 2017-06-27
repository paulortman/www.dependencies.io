---
date: 2017-05-11T11:10:48-05:00
draft: false
title: Generic actors
---

Generic actors don't care about what language or package system a dependency
comes from. They can act on any dependency. Usually this means that they're
limited to simpler notification-style actions (like Slack messages or emails),
since more complex actions usually require working in the same language as
the dependency, with a specific environment.

{{< generic_actors_list >}}
