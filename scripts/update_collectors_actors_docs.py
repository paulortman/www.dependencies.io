from os import path
import datetime
import requests


repos = (
    ('collector', 'python-pip'),
    ('collector', 'js-npm'),
    ('collector', 'git-repo'),
    ('collector', 'php-composer'),
    ('actor', 'python-pip'),
    ('actor', 'js-npm'),
    ('actor', 'repo-issue'),
    ('actor', 'find-replace'),
    ('actor', 'php-composer'),
)


def get_readme_for_repo(type, repo):
    url = 'https://raw.githubusercontent.com/dependencies-io/{}-{}/master/README.md'.format(type, repo)
    response = requests.get(url)
    return response.text.encode('utf-8')


def get_path_for_repo(type, repo):
    p = path.join('content/docs', type + 's', repo + '.md')
    return p


date = datetime.datetime.now().isoformat()

for type, repo in repos:
    print(type, repo)

    readme = get_readme_for_repo(type, repo)
    file_path = get_path_for_repo(type, repo)

    # strip first line (heading) off of readme
    readme = '\n'.join(readme.splitlines()[1:])

    title = '{}: {}'.format(type.capitalize(), repo)

    file_contents = """---
date: {date}
draft: false
title: "{title}"
---

{readme}
""".format(date=date, title=title, readme=readme)

    print 'Writing {}'.format(file_path)

    with open(file_path, 'w+') as f:
        f.write(file_contents)
