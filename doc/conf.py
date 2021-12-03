# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = 'colorcet'
authors = u'Anaconda'
copyright = u'2017-2021 ' + authors
description = 'Collection of perceptually uniform colormaps'

import colorcet
version = release = base_version(colorcet.__version__)

nbbuild_cell_timeout = 10000

html_static_path += ['_static']
html_theme = 'pydata_sphinx_theme'

templates_path = ['_templates']

html_logo = "_static/logo_horizontal.png"
html_favicon = "_static/favicon.ico"
html_css_files = [
    'nbsite.css',
    'custom.css'
]

html_theme_options = {
    "github_url": "https://github.com/holoviz/colorcet",
    "icon_links": [
        {
            # Pointing to Holoviz since colorcet has no dedicated twitter account
            "name": "Twitter",
            "url": "https://twitter.com/HoloViz_org",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.holoviz.org/",
            "icon": "fab fa-discourse",
        }
    ]
}

extensions += [
    'sphinx_copybutton',
]

html_context.update({
    "last_release": f"v{'.'.join(colorcet.__version__.split('.')[:3])}",
    "github_user": "holoviz",
    "github_repo": "colorcet",
    "google_analytics_id": "UA-154795830-4",
})

html_title = f"{project} v{version}"
html_show_sphinx = False
