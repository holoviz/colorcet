# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

###################################################
# edit things below as appropriate for your project

project = u'colorcet'
authors = u'James Bednar'
copyright = u'2017 ' + authors
description = 'A set of useful perceptually uniform colormaps for plotting scientific data.'

version = release = '1.0.0'

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
# logo file etc should be in html_static_path, e.g. _static
html_theme_options = {
#    'custom_css':'bettercolors.css',
#    'logo':'amazinglogo.png',
#    'favicon':'amazingfavicon.ico'
}

_NAV =  (
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'WEBSITE_SERVER': 'https://bokeh.github.io/colorcet',
    'VERSION': version,
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Twitter', '//twitter.com/datashader'),
        ('Github', '//github.com/bokeh/datashader'),
    )
})
