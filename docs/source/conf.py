# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys, time

from .include.snippets import replace_snippets

sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------

project: str = "Sphinx"
author: str = "David J Nevin"
copyright: str = f"{time.strftime('%Y')}, David J Nevin"

# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    # external extensions
    "myst_parser",
    "nbsphinx",
]

myst_enable_extensions = [
    "colon_fence",
    "substitution",
]

# Intersphinx Mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://sphinx-doc.org/en/master/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

# Add any paths that contain custom static files relative to this directory.
# They are copied after the builtin static files.
# Existing files arr overwriten.

html_static_path = ["_static"]

# Text Snippets

# myst_substitutions = {"project": "I'm a **substitution**"}
