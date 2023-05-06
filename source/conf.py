# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SpinalHDL'
copyright = '2018 - ' + str(datetime.date.today().year) + ', SpinalHDL'
author = 'SpinalHDL contributors'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinxcontrib.wavedrom',
    'sphinx_multiversion',
    'sphinx.ext.imgconverter'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_favicon = 'asset/logo/logo3_32x32.png'


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SpinalHDLdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'SpinalHDL.tex', 'SpinalHDL Documentation',
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'spinalhdl', 'SpinalHDL Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'SpinalHDL', 'SpinalHDL Documentation',
     author, 'SpinalHDL', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


html_baseurl = os.getenv('sphinx_html_baseurl', '')

# -- Extension configuration -------------------------------------------------
html_theme_options = {
    # canonical_url is deprecated for html_baseurl
    'canonical_url': os.getenv('sphinx_canonical_url', ''),
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
#    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }

#This is a temporary fix for wavedrom
online_wavedrom_js_url = "https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8"

#Option for linkcheck
linkcheck_anchors=False

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^(master|dev)$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r'^.*$'

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = True

# Run a command before invoking sphinx-build
#smv_prebuild_command = ''

# Regular expression of files and directories to export to outputdir after running smv_prebuild_command
#smv_prebuild_export_pattern = ''

# Export files and directories matching smv_prebuild_export_pattern to this subdirectory of outputdir
#smv_prebuild_export_destination = ''

# Specify build targets and whether the resulting artefacts should be downloadable
smv_build_targets = {
    "HTML" : {
        "builder": "html",
        "downloadable": False,
        "download_format": "",
    },
    "SingleHTML" : {
        "builder": "singlehtml",
        "downloadable": True,
        "download_format": "zip",
    },
    "PDF" : {
        "builder": "latexpdf",
        "downloadable": True,
        "download_format": "pdf",
    }
}

# Flag indicating whether the intermediate build directories should be removed after artefacts are produced
smv_clean_intermediate_files = True

# This is in the project as bin/convert-wrapper, check we are setup correctly.
have_image_converter = subprocess.call(['which', 'convert-wrapper'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
if have_image_converter:
    image_converter='convert-wrapper'
else:
    print("ERROR: convert-wrapper not found in $PATH, did you: source $PWD/bin/setup_env.sh", file=sys.stderr)
    sys.exit(1)

