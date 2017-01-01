#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found")
    read_md = lambda f: open(f, 'r').read()


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

readme = read_md('README.md')


setup(
    name='bottlejwt',
    version='0.0.6',
    description='JWT plugin for bottle',
    long_description=readme,
    author='Alberto Galera Jimenez',
    author_email='galerajimenez@gmail.com',
    url='https://github.com/kianxineki/bottlejwt',
    py_modules=['bottlejwt'],
    include_package_data=True,
    install_requires=['pyjwt', 'bottle'],
    license="GPL",
    zip_safe=False,
    keywords='bottlejwt',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    entry_points={}
)
