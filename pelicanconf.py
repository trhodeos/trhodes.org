#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tyler Rhodes'
SITENAME = 'trhodes.org'
SITEURL = ''

THEME = 'themes/pelican-hyde'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DISPLAY_PAGES_ON_MENU = True

DEFAULT_LANG = 'en'

PROFILE_IMAGE = 'self.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
        ('email', 'tyler@trhodes.org'),
        ('linkedin', 'https://www.linkedin.com/in/tyler-rhodes-7a42a023'),
        ('github', 'https://github.com/trhodeos'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
