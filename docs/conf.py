# Copyright 2024 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

from tdoc.common.defaults import *

project = "Informatique"
author = "Caroline Blank"
license = 'CC-BY-NC-SA-4.0'
language = 'fr'

exclude_patterns = ['_include/**']
myst_links_external_new_tab = True
myst_footnote_transition = False

html_static_path = ['_static.export']
html_css_files = ['tdoc/exec-pnm.css', 'site-styles.css']
html_theme_options = {
    'repository_url': 'https://github.com/t-doc-org/informatique',
    'show_navbar_depth': 2,
    'show_toc_level': 2,
}

metadata = {
    'points': {
        'text': [" ({0} pt)", " ({0} pts)"],
    },
    'exec': {'pnm': {}},
}
