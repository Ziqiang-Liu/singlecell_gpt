# sphinx-apidoc -o ./docs/source ./code
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
print('sys.path', sys.path)
print('list dir', os.listdir(sys.path[0]))


# -- Project information -----------------------------------------------------

project = 'single-cell gpt'
copyright = '2023, qiliu'
author = 'qiliu'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    # 'sphinx.ext.autosummary',
    'sphinx_rtd_theme',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    # "nbsphinx",
    # 'nbsphinx_link',
    'sphinx_markdown_tables'
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,
}

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'numpy': ('https://numpy.org/doc/stable/', None),
#     'PyTorch': ('https://pytorch.org/docs/stable/', None),
# }

show_authors = True

napoleon_use_ivar = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# autodoc_mock_imports = ['loris', 'readline', '_C_gemm', '_C_neuron', 'torchaudio', 'onnx', 'onnxruntime', 'gym', 'cloudpickle', 'rarfile', 'lava', 'lyngor', 'lynpy', 'sklearn', 'h5py']
# autoclass_content = 'both'
# autodoc_member_order = 'bysource'
# autodoc_inherit_docstrings = False

# master_doc = 'index'

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.



# Generate the API documentation when building
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'preamble': r'\setcounter{tocdepth}{3}',
}
