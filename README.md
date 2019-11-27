# Overview

The official command-line client for [The Coverage Space](http://coverage.space).

[![Unix Build Status](https://img.shields.io/travis/jacebrowning/coverage-space-cli/master.svg?label=unix)](https://travis-ci.org/jacebrowning/coverage-space-cli)
[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/coverage-space-cli/master.svg?label=window)](https://ci.appveyor.com/project/jacebrowning/coverage-space-cli)
[![Coverage Status](https://img.shields.io/coveralls/jacebrowning/coverage-space-cli/master.svg)](https://coveralls.io/r/jacebrowning/coverage-space-cli)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/coverage-space-cli.svg)](https://scrutinizer-ci.com/g/jacebrowning/coverage-space-cli/?branch=master)
[![PyPI Version](https://img.shields.io/pypi/v/coveragespace.svg)](https://pypi.org/project/coveragespace)
[![PyPI License](https://img.shields.io/pypi/l/coveragespace.svg)](https://pypi.org/project/coveragespace)

# Setup

## Requirements

* Python 3.5+

## Installation

Install this library directly into an activated virtual environment:

```text
$ pip install coveragespace
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add coveragespace
```

# Usage

To update the value for a test coverage metric:

```sh
$ coveragespace <owner/repo> <metric>
```

For example, after testing with code coverage enabled:

```sh
$ coveragespace owner/repo unit
```

will attempt to extract the current coverage data from your working tree and compare that with the last known value. The coverage value can also be manually specified:

```sh
$ coveragespace <owner/repo> <metric> <value>
```
