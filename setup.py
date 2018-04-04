#!/usr/bin/env python3

from setuptools import setup

setup(name='genice-diffr',
      version='0.1',
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
      keywords=['genice',],
      license='MIT',
      packages=[
                'genice.formats',
                ],
      install_requires=['genice>=0.16', 'countrings>=0.1.4'],
      )

