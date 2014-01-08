#!/usr/bin/env python

from setuptools import setup, find_packages

modules = ['feedshare', 'feedshare.feedlists', 'feedshare.feedlists.management.commands']

setup(
    name='feedshare',
    version='0.1',
    description='Feedshare is a service to share and discover OPML feed lists.',
    author='Arne Holzenburg',
    author_email='arne@holzenburg.de',
    url='https://github.com/holzenburg/feedshare/',
    #packages=find_packages(),
    py_modules=modules,
    license='License :: GNU GENERAL PUBLIC LICENSE',

    # Enable django-setuptest
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        # Required by django-setuptools on Python 2.6
        'argparse'
        ),
    )
