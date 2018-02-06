# -*- coding: utf-8 -*-

AUTHOR = u'Matt Makai'
SITENAME = u'Deploy Python'
SITEURL = 'http://www.deploypython.com'
TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/mattmakai/deploypython.com'
PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index','sitemap')

ARTICLE_SAVE_AS = 'blog/{slug}.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
FEED_DOMAIN = 'http://www.deploypython.com/'

LINKS = ()
MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/mattmakai'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

