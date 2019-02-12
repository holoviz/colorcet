# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = 'colorcet'
authors = u'Anaconda'
copyright = u'2019 ' + authors
description = 'Collection of perceptually uniform colormaps'

import colorcet
version = release = colorcet.__version__

nbbuild_cell_timeout = 10000

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
# logo file etc should be in html_static_path, e.g. _static


html_theme_options = {
    'logo':'logo.png',
    'favicon':'favicon.ico',
    'custom_css':'site.css'
}

_NAV = (
    ('Introduction', 'index'),
    ('Getting Started', 'getting_started/index'),
    ('User Guide', 'user_guide/index'),
    ('About', 'about'),
)

_SOCIAL = (
    ('Gitter', '//gitter.im/pyviz/pyviz'),
    ('Github', '//github.com/pyviz/' + project),
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'WEBSITE_SERVER': 'http://{}.pyviz.org'.format(project),
    'VERSION': version,
    'NAV': _NAV ,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': _SOCIAL
})
