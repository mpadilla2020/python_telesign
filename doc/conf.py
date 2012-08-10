# -*- coding: utf-8 -*-
#
# TeleSign REST API documentation build configuration file, created by sphinx-quickstart on Mon Apr  9 14:35:45 2012.
# This file is execfile()d with the current directory set to its containing dir.
# Note that not all possible configuration values are present in this autogenerated file.
# All configuration values have a default; values that are commented-out serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory, add these directories to sys.path here. If the directory is relative to the documentation root, use os.path.abspath to make it absolute, like shown here.sys.path.insert(0, os.path.abspath('.')).

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

# Add any paths that contain templates here, relative to this directory (\doc\).
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'TeleSign Python SDK'
copyright = u'2012, TeleSign Corporation'

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
# We're not exposing the Account class publically.
exclude_patterns = ['api/generated/telesign.api.Account.rst']

# html_add_permalinks = ''

# The reST default role (used for this markup: `text`) to use for all documents.
# Note: Empiraclly shown to be <cite>.
#default_role = None

# If true, the current module name will be prepended to all description unit titles (such as .. function::).
#add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'telesign'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# This value selects if automatically documented members are sorted alphabetical (value 'alphabetical'), by member type (value 'groupwise') or by source order (value 'bysource'). The default is alphabetical. Note that for source order, the module must be a Python module with the source code available.
autodoc_member_order = 'bysource'

# -- Options for HTML output ---------------------------------------------------

# Add the TeleSign logo to the docs.
html_logo = '_static/telesign-logo-small.jpg'

# The theme to use for HTML and HTML Help pages. See the documentation for a list of builtin themes: http://sphinx.pocoo.org/theming.html.
html_theme = 'telesign'

# Theme options are theme-specific and customize the look and feel of a theme further.  For a list of options available for each theme, see the documentation.
# Note: These settings will be incorporated into the auto-generated style sheet: default.css.
html_theme_options = {
    'sidebarbgcolor': 'white',
    'sidebartextcolor': '#5A5A5A',
    'sidebarlinkcolor': '004B8C',
    'bodyfont': 'sans-serif',
    'headfont': 'sans-serif',
    'footerbgcolor': '#969696',
    'codebgcolor': '#FAFAD2',
    'headbgcolor': 'white',
    'headtextcolor': '#004B8C',
    'relbarbgcolor': '#004B8C',
    'textcolor': '#000000',
    'linkcolor': '#0078AF',
    'visitedlinkcolor': '#0078AF'
}

# Change the Table of Contents from "localtoc.html" to "globaltoc.html".
html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'searchbox.html'],
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory. They are copied after the builtin static files, so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom, using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will contain a <link> tag referring to it.  The value of this option must be the base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'TeleSignRESTAPIdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'TeleSignRESTAPI.tex', u'TeleSign REST API Documentation',
   u'TeleSign', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts, not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'telesignrestapi', u'TeleSign REST API Documentation',
     [u'TeleSign'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples(source start file, target name, title, author, dir menu entry, description, category).
texinfo_documents = [
  ('index', 'TeleSignRESTAPI', u'TeleSign REST API Documentation',
   u'TeleSign', 'TeleSignRESTAPI', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'
