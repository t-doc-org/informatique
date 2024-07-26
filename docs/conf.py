# Copyright 2024 Caroline Blank <caro@c-space.org>
# Copyright 2024 Remy Blank <remy@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

project = "Informatique"
html_title = "Informatique"
copyright = "2024 Caroline Blank"
language = 'fr'

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.imgconverter',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_togglebutton',
]
myst_enable_extensions = [
    'amsmath',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    # 'linkify',
    # 'replacements',
    # 'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
]

# templates_path = ['_templates']
# html_static_path = ['_static']

exclude_patterns = [
    '_build',
    '.DS_Store',
    'Thumbs.db',
]

html_theme = 'sphinx_book_theme'
html_theme_options = {
    'use_sidenotes': True,
    # 'show_prev_next': False,
}

myst_dmath_double_inline = True
myst_substitutions = {
}
