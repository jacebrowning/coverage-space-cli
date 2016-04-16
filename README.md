# The Coverage Space (CLI)

Command-line client for The Coverage Space.

[![Build Status](http://img.shields.io/travis/jacebrowning/coverage-space-cli/develop.svg)](https://travis-ci.org/jacebrowning/coverage-space-cli)
[![Coverage Status](http://img.shields.io/coveralls/jacebrowning/coverage-space-cli/develop.svg)](https://coveralls.io/r/jacebrowning/coverage-space-cli)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/jacebrowning/coverage-space-cli.svg)](https://scrutinizer-ci.com/g/jacebrowning/coverage-space-cli/?branch=develop)
[![PyPI Version](http://img.shields.io/pypi/v/coverage.space.svg)](https://pypi.python.org/pypi/coverage.space)
[![PyPI Downloads](http://img.shields.io/pypi/dm/coverage.space.svg)](https://pypi.python.org/pypi/coverage.space)

## Getting Started

### Requirements

* Python 2.7+ or Python 3.3+

### Installation

The client can be installed with pip:

```
$ pip install --upgrade coverage.space
```

or directly from the source code:

```
$ git clone https://github.com/jacebrowning/coverage-space-cli.git
$ cd coverage-space-cli
$ python setup.py install
```

## Basic Usage

To update the value for a test coverage metric:

```
$ coverage.space <owner/repo> <metric>
```

For example:

```
$ coverage.space owner/repo unit
```

This will attempt to extract the current coverage data from your working tree.
The coverage value can also be manually specified:

```
$ coverage.space <owner/repo> <metric> <value>
```

## Documentation

Read the full documentation [here](http://coverage.space/client/).
