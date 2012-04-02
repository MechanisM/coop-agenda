#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

VERSION = __import__('coop_agenda').__version__

import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='coop-agenda',
    version = VERSION,
    description='Companion app for django-coop, a fork of swingtime',
    packages=[  'coop_agenda',
                'coop_agenda.conf'
                ],
    include_package_data=True,
    author='Dominique Guardiola',
    author_email='dguardiola@quinode.fr',
    license='BSD',
    zip_safe=False,
    long_description = open('README.rst').read(),
    url = 'https://github.com/quinode/coop_agenda/',
    download_url = 'https://github.com/quinode/coop_agenda/tarball/master',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Natural Language :: English',
        'Natural Language :: French',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],

)

