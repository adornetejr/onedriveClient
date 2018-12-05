#!/usr/bin/env python3

"""
onedrive-d
A Microsoft OneDrive client for Linux.
:copyright: (c) Xiangyu Bu
:license: MIT
"""

import sys
from setuptools import setup, find_packages

from onedrive_client import __author__, __email__, __homepage__, __project__, __version__


with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

test_requires = [
    'requests-mock',
]

with open('README.md', 'r') as f:
    readme = f.read()

python_version = sys.version_info

if python_version < (3, 4):
    raise Exception('%s %s only supports Python 3.4 and newer.' % (__project__, __version__))

if python_version < (3, 5):
    install_requires.append('dbus-python')

setup(
    name=__project__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    url=__homepage__,
    description='A Microsoft OneDrive client for Linux written in Python 3.',
    license='MIT',
    long_description=readme,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    package_data={
            'onedrive_client': ['data/*', 'lang/*']
    },
    package_dir={'onedrive_client': 'onedrive_client'},
    entry_points={
        'console_scripts': [
            'onedrive-client = onedrive_client.od_main:main',
            'onedrive-client-pref = onedrive_client.od_pref:main'
        ],
        'gui_scripts': []
    },
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite='tests',
    zip_safe=False
)
