#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import os
import re
import sys


VERSION_FILE = 'grappelli_extras/__init__.py'
version_text = open(VERSION_FILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, version_text, re.M)
if mo:
    version = mo.group(1)
    print (version)
else:
    raise RuntimeError(
        "Unable to find version string in %s." % (VERSION_FILE,))

name = 'django-grappelli-extras'
package = 'grappelli_extras'
description = 'Ajax, Extensions and Extras for Grappelli Admin interface'
url = 'https://github.com/xangcastle/grappelli_extras/'
author = 'Cesar Abel Ramirez'
author_email = 'xangcastle@gmail.com'
license = 'BSD'
install_requires = [
    'django-grappelli>=2.11.1',
    'django-import-export>=1.0.1',
    'django-adminactions>=1.5 ',
]

if sys.argv[-1] == 'publish':
    args = {'version': version}
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/django-grappelli-extras-%(version)s*" % args)
    print("Creating git tag the version now:")
    os.system("git tag -a %(version)s -m 'version %(version)s'" % args)
    os.system("git push --tags")
    sys.exit()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), "r").read()


setup(
    name=name,
    version=version,
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    packages=['grappelli_extras'],
    include_package_data=True,
    description=description,
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
    install_requires=install_requires
)
