#!/usr/bin/env python

"""Setup script for The Coverage Space CLI."""

import setuptools

from coveragespace import __project__, __version__, CLI

try:
    README = open("README.rst").read()
    CHANGELOG = open("CHANGELOG.rst").read()
except IOError:
    LONG_DESCRIPTION = "<placeholder>"
else:
    LONG_DESCRIPTION = README + '\n' + CHANGELOG

setuptools.setup(
    name=__project__,
    version=__version__,

    description="A place to track your code coverage metrics.",
    url='https://github.com/jacebrowning/coverage-space-cli',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [
        CLI + ' = coveragespace.cli:main',
    ]},

    long_description=LONG_DESCRIPTION,
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
    dependency_links = [
        'https://github.com/chrippa/backports.shutil_get_terminal_size/tarball/159e269450dbf37c3a837f6ea7e628d59acbb96a#egg=backports.shutil-get-terminal-size'
    ]
)
