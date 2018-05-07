#!/usr/bin/env python

# from distutils.core import setup, Extension
from setuptools import setup, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs
import os
import codecs
import re

#Copied from wheel package
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.dirname(__file__), 'genice_diffr', '__init__.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))
    

setup(
    name='genice_diffr',
    version=metadata['version'],
    description='Diffraction plugin for GenIce.',
    #long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ],
    author='Masakazu Matsumoto',
    author_email='vitroid@gmail.com',
    url='https://github.com/vitroid/genice-diffr/',
    keywords=['genice', 'diffraction', 'yaplot'],

    packages=['genice_diffr',
              'genice_diffr.formats',
    ],
    
    entry_points = {
        'genice_format_hook1': [
            '_Diffr      = genice_diffr.formats._Diffr:hook1',
        ],
        'genice_format_hook0': [
            '_Diffr      = genice_diffr.formats._Diffr:hook0',
        ],
    },
    install_requires=['yaplotlib', 'contour3d', 'GenIce>=0.23'],

    license='MIT',
)
