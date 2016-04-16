"""Update project metrics on The Coverage Space.

Usage:
  coverage.space <owner/repo> <metric> [<value>] [--exit-code]
  coverage.space (-h | --help)
  coverage.space (-V | --version)

Options:
  -h --help         Show this help screen.
  -V --version      Show the program version.
  --exit-code       Return non-zero exit code on failures.

"""

from __future__ import unicode_literals

import sys
import json

import six
from docopt import docopt
import blessings
import requests

from . import API, VERSION

from .plugins import get_coverage

term = blessings.Terminal()


def main():
    """Run the program."""
    arguments = docopt(__doc__, version=VERSION)

    slug = arguments['<owner/repo>']
    metric = arguments['<metric>']
    value = arguments.get('<value>') or get_coverage()

    success = call(slug, metric, value)

    if not success and arguments['--exit-code']:
        sys.exit(1)


def call(slug, metric, value):
    """Call the API and display errors."""
    url = "{}/{}".format(API, slug)
    data = {metric: value}

    response = requests.put(url, data=data)

    if response.status_code == 200:
        return True

    elif response.status_code == 422:
        display("coverage decreased", response.json(), term.bold_yellow)
        return False

    else:
        display("coverage unknown", response.json(), term.bold_red)
        return False


def display(title, data, color=term.normal):
    """Write colored text to the console."""
    width = term.width or 80
    six.print_(color("{0:=^{1}}".format(' ' + title + ' ', width)))
    six.print_(color(json.dumps(data, indent=4)))
    six.print_(color('=' * width))
