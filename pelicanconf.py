#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Roman Luštrik'
SITENAME = 'Roman Luštrik not Inc.'
SITEURL = 'http://biolitika.si'

PATH = 'content'

TIMEZONE = 'Europe/Ljubljana'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = False
CATEGORY_FEED_ATOM = False
TRANSLATION_FEED_ATOM = False
AUTHOR_FEED_ATOM = False
AUTHOR_FEED_RSS = False
TAG_FEED_RSS = True

RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (
            ('visit me on StackOverFlow', 'https://stackoverflow.com/users/322912/roman-lu%C5%A1trik'),
            ('#metamorfoza podcast (SI)', 'http://metinalista.si/category/metamorfoza'),
            ('r-bloggers', 'https://www.r-bloggers.com'),
        )

# Social widget
SOCIAL = (
            ('GitHub', 'https://github.com/romunov'),
            ('Twitter', 'https://twitter.com/romunov'),
            ('LinkedIn', 'https://www.linkedin.com/in/roman-lu%C5%A1trik-5a6586ab'),
        )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./raw_themes/pelican-blueidea"

# pelican-blueidea theme settings:
# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = (True)

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = (True)

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = (False)

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = (False)

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = (False)

# Display the search form
DISPLAY_SEARCH_FORM = (False)

# Sort pages list by a given attribute
#PAGES_SORT_ATTRIBUTE = (Date)

# Display the "Fork me on Github" banner
# GITHUB_URL = ('https://github.com/romunov/pelican-blueidea')

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

STATIC_PATHS= ['images', 'extra/CNAME', 'gross_cumsum_salary_files']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
OUTPUT_PATH = 'docs/'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', 'CNAME']

