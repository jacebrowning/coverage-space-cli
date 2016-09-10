#!/usr/bin/env python

"""Setup script for The Coverage Space CLI."""

import os
import sys

import setuptools


PACKAGE_NAME = 'coveragespace'
MINIMUM_PYTHON_VERSION = 2, 7


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {}.{}+ is required.".format(*MINIMUM_PYTHON_VERSION))


def read_package_variable(key):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, '__init__.py')
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ')
            if parts and parts[0] == key:
                return parts[-1].strip("'")
    assert 0, "'{0}' not found in '{1}'".format(key, module_path)


def read_descriptions():
    """Build a description for the project from documentation files."""
    try:
        readme = open("README.rst").read()
        changelog = open("CHANGELOG.rst").read()
    except IOError:
        return "<placeholder>"
    else:
        return readme + '\n' + changelog


check_python_version()
setuptools.setup(
    name=read_package_variable('__project__'),
    version=read_package_variable('__version__'),

    description="A place to track your code coverage metrics.",
    url='https://github.com/jacebrowning/coverage-space-cli',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [
        'coverage.space = coveragespace.cli:main',
    ]},

    long_description=read_descriptions(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],

    install_requires=open("requirements.txt").readlines(),
    dependency_links=[
        'https://github.com/chrippa/backports.shutil_get_terminal_size/tarball/159e269450dbf37c3a837f6ea7e628d59acbb96a#egg=backports.shutil-get-terminal-size'
    ]
)
