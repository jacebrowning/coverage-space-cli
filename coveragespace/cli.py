"""Update project metrics on The Coverage Space.

Usage:
  coverage.space <owner/repo> <metric> [<value>] [--verbose] [--exit-code]
  coverage.space (-h | --help)
  coverage.space (-V | --version)

Options:
  -h --help         Show this help screen.
  -V --version      Show the program version.
  -v --verbose      Always display the coverage metrics.
  --exit-code       Return non-zero exit code on failures.

"""

from __future__ import unicode_literals

import sys
import json

import six
from docopt import docopt
import requests
import colorama
from backports.shutil_get_terminal_size import get_terminal_size

from . import API, VERSION

from .plugins import get_coverage
from .cache import Cache


cache = Cache()


def main():
    """Run the program."""
    colorama.init(autoreset=True)
    arguments = docopt(__doc__, version=VERSION)

    slug = arguments['<owner/repo>']
    metric = arguments['<metric>']
    value = arguments['<value>'] or get_coverage()
    verbose = arguments['--verbose']
    hardfail = arguments['--exit-code']

    success = call(slug, metric, value, verbose, hardfail)

    if not success and hardfail:
        sys.exit(1)


def call(slug, metric, value, verbose=False, hardfail=False):
    """Call the API and display errors."""
    url = "{}/{}".format(API, slug)
    data = {metric: value}

    response = cache.get(url, data)
    if response is None:
        response = requests.put(url, data=data)
        cache.set(url, data, response)

    if response.status_code == 200:
        if verbose:
            display("coverage increased", response.json(), colorama.Fore.GREEN)
        return True

    elif response.status_code == 422:
        color = colorama.Fore.RED if hardfail else colorama.Fore.YELLOW
        display("coverage decreased", response.json(), color)
        return False

    else:
        display("coverage unknown", response.json(), colorama.Fore.RED)
        return False


def display(title, data, color=""):
    """Write colored text to the console."""
    color += colorama.Style.BRIGHT
    width, _ = get_terminal_size()
    six.print_(color + "{0:=^{1}}".format(' ' + title + ' ', width))
    six.print_(color + json.dumps(data, indent=4))
    six.print_(color + '=' * width)
