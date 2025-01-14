import sys
import os

sys.path.append(os.path.abspath('..'))
project = 'Rest API'
copyright = '2023, Y'
author = 'Y'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static']
html_theme = 'nature'

