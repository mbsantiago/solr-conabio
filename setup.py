# -*- coding: utf-8 -*-
from setuptools import setup
import os


SHORT_DESCRIPTION = 'Easy Solr quering'
URL = 'http://github.com/mbsantiago/solr-conabio'
AUTHOR = 'Santiago Martínez, CONABIO'
AUTHOR_EMAIL = 'santiago.mbal@gmail.com'
VERSION = None
PACKAGE = 'solr_conabio'


HERE = os.path.abspath(os.path.dirname(__file__))


# Read version
version = {}
with open(os.path.join(HERE, PACKAGE, '__version__.py'), 'r') as version_file:
    exec(version_file.read(), version)
    VERSION = version['__version__']

# Read long description
with open('README.md', 'r') as readme_file:
    LONG_DESCRIPTION = readme_file.read()


setup(name='solr-conabio',
      version=VERSION,
      description=SHORT_DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license='MIT',
      packages=[PACKAGE],
      install_requires=['requests', 'six'],
      zip_safe=False)
