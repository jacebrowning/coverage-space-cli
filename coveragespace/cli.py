"""Update project metrics on The Coverage Space.

Usage:
  coverage.space <owner/repo> <metric> [<value>]
  coverage.space (-h | --help)
  coverage.space (-V | --version)

Options:
  -h --help     Show this screen.
  -V --version     Show version.

"""

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

    sys.exit(success)


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
    six.print_(color("{t:=^{w}}".format(t=' ' + title + ' ', w=term.width)))
    six.print_(color(json.dumps(data, indent=4)))
    six.print_(color('=' * term.width))
