#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
 
setup(
    name='sjuxax-facebook',
    version='0.1',
    description='Download profile pictures correctly using Facebook\'s Python SDK',
    author='Facebook; sjuxax',
    url='http://github.com/sjuxax/python-sdk',
    package_dir={'': 'src'},
    py_modules=[
        'facebook',
    ],
)
