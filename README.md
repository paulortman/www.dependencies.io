# www.dependencies.io

Run local hugo server and gulp for compiling assets:
```sh
$ npm run dev
```

Where things are:
- Homepage is at `layouts/index.html`
- Other one-off pages are in the root of `content`. They have frontmatter which tell
hugo what url they should be located at
- Documentation content is in `content/docs` and everything inside is published based on the path
