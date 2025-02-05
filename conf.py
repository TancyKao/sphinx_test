# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os


project = 'TK'
copyright = '2024, TK'
author = 'TK'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# General configuration
extensions = ['sphinx_rtd_theme']
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_output = os.environ.get('READTHEDOCS_OUTPUT', '_build/html')
html_build_dir = os.path.join(html_output_dir, 'html')