Title: How to build a static website using Pelican
Date: 2018-03-19
Category: HowTo
Tags: pelican

It's fairly easy to build a static website. Static websites differ from dynamic in that they do not communicate with a database of any sorts. This makes it easier and especially cheaper to deploy to almost any setup which runs at least rudimentary serving capabilities.

There are many options for static site generation, I chose [Pelican](http://docs.getpelican.com/en/stable/quickstart.html). There is no particular adamant reason behind it, but [browsing for themes](http://pelicanthemes.com/) did tilt the scales in its favor.

Workflow is basically simple. One time install is that of `Python` (e.g. version 3.6). Once you have that, I would recommend you also get `pip install virtualenvwrapper`.

You then activate virtual environment and install all dependencies for `pelican`.

```
# create and activate virtual environment
mkvirtenv mystaticwebsite
workon mystaticwebsite

# installs pelican
pip install pelican
```

Create your project folder

```
mkdir mywebsite
cd mywebsite
```

Now feel free to follow [instructions from `pelican-quickstart`](http://docs.getpelican.com/en/stable/quickstart.html) on.

Once you are done writing contents to a markdown (`.md`) file you 'publish' your website, which puts all the bits and pieces together (applies settings, theme...) into an `/output` folder. You can do that using `pelican content --output output --ignore-cache --relative-urls --settings publishconf.py`. Making paths relative enables you to view your site locally without resorting to changing `SITEURL = ''` before compiling.

To make your website ready to be published, feel free to include settings specified in the `publishconf.py`, e.g. `pelican content --output output --ignore-cache --settings publishconf.py`. Ignoring cache will make sure some weird bits do not get left in and Pelican starts afresh.
