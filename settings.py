# -*- coding: utf-8 -*-

AUTHOR = u'Matthew Makai'
SITENAME = u'Deploy Python'
SITEURL = 'https://www.deploypython.com'
TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/mattmakai/deploypython.com'
PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index','sitemap','deploying-flask-web-apps',
                    'full-stack-python')

ARTICLE_SAVE_AS = 'blog/{slug}.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
FEED_DOMAIN = 'https://www.deploypython.com/'

LINKS = ()
MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/mattmakai'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

