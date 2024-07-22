project = 'The Hitchhiker’s Guide to LLMs for Events'
copyright = '2024, ExpoPlatform'
author = 'ExpoPlatform'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
]
source_suffix = [".rst", ".md"]

templates_path = ['_templates']
exclude_patterns = []

language = "English"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"
]

# Need for MyST-NB extension
suppress_warnings = ["mystnb.unknown_mime_type"]

# Turn off notebooks execution
nb_execution_mode = "off"

myst_heading_anchors = 4
