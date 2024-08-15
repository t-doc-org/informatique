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
html_theme_options['extra_footer'] = f"""\
Copyright {copyright}, \
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">\
CC-BY-NC-SA-4.0</a>\
"""
