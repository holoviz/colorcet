# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = 'colorcet'
authors = u'Anaconda'
copyright = u'2017-2021 ' + authors
description = 'Collection of perceptually uniform colormaps'

import colorcet
version = release = base_version(colorcet.__version__)

nbbuild_cell_timeout = 10000

exclude_patterns = ['governance']
html_static_path += ['_static']
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/logo_horizontal.png"
html_favicon = "_static/favicon.ico"
html_css_files += [
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
    ],
    "footer_items": [
        "copyright",
        "last-updated",
    ],
}

extensions += [
    'sphinx_copybutton',
    'nbsite.analytics',
]

nbsite_analytics = {
    'goatcounter_holoviz': True,
}

html_context.update({
    "github_user": "holoviz",
    "github_repo": "colorcet",
})

# Override the Sphinx default title that appends `documentation`
html_title = f"{project} v{version}"
# Format of the last updated section in the footer
html_last_updated_fmt = "%Y-%m-%d"
