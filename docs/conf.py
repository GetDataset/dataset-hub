import os
import sys

sys.path.insert(0, os.path.abspath(".."))  # чтобы Sphinx видел dataset_hub

project = "DatasetHub"
author = "Slava Bakulin"
release = "0.1.0"


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "en"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]

# Настройки автодокументации
autodoc_member_order = "bysource"
autodoc_typehints = "description"

autodoc_default_options = {
    "members": False,
    "undoc-members": False,
}
autosummary_generate = False
