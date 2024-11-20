# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'libdocument'
copyright = '2023, MQChen'
author = 'MQChen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables'
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'


pygments_style = 'sphinx'


numfig= True
numfig_secnum_depth = 2

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output



html_theme = 'furo'
html_static_path = ['_static']

html_show_sourcelink = False

