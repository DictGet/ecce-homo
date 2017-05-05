# -*- coding: utf-8 -*-
#! /usr/bin/env python
import os
import subprocess
from setuptools import setup

import six

here = os.path.dirname(os.path.abspath(__file__))
README = open(os.path.join(here, 'README.md')).read()
REQUIREMENTS = open(os.path.join(here, 'requirements/base.txt')).readlines()

def get_version_from_git_tag():
    command = "git describe --abbrev=0 --tags"
    if six.PY2:
        return subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT).strip()

    return subprocess.getoutput(command).strip()

scripts = {
    "console_scripts": [
        "eccehomo=eccehomo.app:app",
    ]
}

setup(
    name='eccehomo',
    version=get_version_from_git_tag(),
    description='Micro application to serve images with customized cropping',
    long_description=README,
    author='DictGet Team',
    author_email='dictget@gmail.com',
    url="https://github.com/dictget/ecce-homo",
    download_url="https://github.com/dictget/ecce-homo/archive/{}.tar.gz".format(
        get_version_from_git_tag()
    ),
    packages=['eccehomo'],
    test_suite="eccehomo.tests",
    entry_points=scripts,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
