#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

read_md = lambda f: open(f, 'r', encoding="utf-8").read()

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
    version='1.0.2',
    description='JWT plugin for bottle',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Alberto Galera Jimenez',
    author_email='galerajimenez@gmail.com',
    url='https://github.com/agalera/bottlejwt',
    py_modules=['bottlejwt'],
    include_package_data=True,
    install_requires=['pyjwt==2.8.0'],
    license="GPL",
    zip_safe=False,
    keywords='bottlejwt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    entry_points={}
)
