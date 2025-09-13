title: Build Pelican static website using GitHub actions
date: 2020-08-06 20:18
tags:
keywords: static website, pelican, git, github, actions, CI/CD, python
category: HowTo
slug: build-pelican-static-website-using-github-actions
author: Roman Luštrik
summary: It is easy to automatically build Pelican static website and deploy it to GitHub Pages using GitHub actions.
translation: false
status: published
lang: en

GitHub enables the delivery of static contents using [GitHub Pages](https://pages.github.com/). That is, you create a GitHub repository and serve it as a regular static website. For most use cases I need, this is more than enough.

I use Pelican to create a static website from `.md` files. This content resides within the `master` branch of my repository and consists of theme folder, content (where my blog posts are saved), `Makefile` and some configuration files. Since I'm serving my website to a custom domain (and not just romunov.github.io), I also have a `./content/extra/CNAME` entry with `biolitika.si` for the re-routing to work.

To get the GitHub workflow running, I created a `.github/workflows/build-blog.yml` file with the following content:

```
name: Deploy biolitika blog
on:
  push:
    branches:
      - master
jobs:
  build_job:
    name: Deploy blog
    runs-on: ubuntu-latest
    steps:
      - name: Install Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.7
      - name: Checkout website source
        id: checkout-master
        uses: actions/checkout@v2
      - name: Cache dependencies
        uses: actions/cache@v2
        with:
          path: ~/.cache/pip
          key: pelican-4.2.0-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            pelican-4.2.0-
      - name: Install Pelican
        run: |
          pip install -r requirements.txt
      - name: Run Pelican
        id: run-pelican
        run: |
          pelican content --output docs --settings publishconf.py
      - name: Push to GitHub pages
        id: push-to-gh-pages
        run: |
          git config --global user.name "my username"
          git config --global user.email "myemail@provider.com"

          git add docs/
          git commit --amend --no-edit

          git push origin master:deploy --force

```

Once you commit this file, a new Workflow should appear in GitHub Actions tab.

<img src="{static}/images/gh_actions.png" width="760">

The detail important for this case is that once Pelican creates a `docs/` folder, new changes are pushed to a new branch called `deploy`. I have configured this repository so that the static content is served from `deploy` branch, `docs/` folder.

Every time I submit new commit(s), workflow is triggered (on push) and new contents delivered.
