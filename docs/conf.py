# Copyright 2024 Caroline Blank <caro@c-space.org>
# Copyright 2024 Remy Blank <remy@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import time

from tdoc.common.defaults import *

project = "Informatique"
copyright = f"{time.strftime('%Y')} Caroline Blank"

html_title = project
html_short_title = html_title

keep_warnings = True

html_show_copyright = False
html_theme_options.update({
    'repository_url': 'https://github.com/t-doc-org/informatique',
    'repository_branch': 'main',
    'path_to_docs': 'docs',
    "use_repository_button": True,
    'use_source_button': True,
    'extra_footer': f"""\
Copyright {copyright}, \
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">\
CC-BY-NC-SA-4.0</a>\
""",
})
