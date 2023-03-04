# Configuration file for the Sphinx documentation builder.
project = 'DevOps'
copyright = '2023, skillab'
author = 'skillab'
release = '1'

import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'recommonmark',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

pygments_style = 'sphinx'

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

html_theme_options = {
    "navigation_depth": -1
}

html_logo = "_static/Logo.jpg"

html_css_files = ['max_width.css']
