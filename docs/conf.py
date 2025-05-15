# Copyright 2024 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

from tdoc.common.defaults import *

project = "Informatique"
copyright = "%Y Caroline Blank"
license = 'CC-BY-NC-SA-4.0'
language = 'fr'

myst_links_external_new_tab = True

html_theme_options = {
    'repository_url': 'https://github.com/t-doc-org/informatique',
}

# tdoc_solutions = 'dynamic'
tdoc = {
    'api_url': 'https://api.t-doc.org' if 'tdoc-dev' not in tags else None,
}
