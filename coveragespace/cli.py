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
    value = arguments.get('<value>') or get_coverage()

    success = call(slug, metric, value)

    if not success and arguments['--exit-code']:
        sys.exit(1)


def call(slug, metric, value):
    """Call the API and display errors."""
    url = "{}/{}".format(API, slug)
    data = {metric: value}

    response = cache.get(url, data)
    if response is None:
        response = requests.put(url, data=data)
        cache.set(url, data, response)

    if response.status_code == 200:
        return True

    elif response.status_code == 422:
        display("coverage decreased", response.json(),
                colorama.Fore.YELLOW + colorama.Style.BRIGHT)
        return False

    else:
        display("coverage unknown", response.json(),
                colorama.Fore.RED + colorama.Style.BRIGHT)
        return False


def display(title, data, color=""):
    """Write colored text to the console."""
    width, _ = get_terminal_size()
    six.print_(color + "{0:=^{1}}".format(' ' + title + ' ', width))
    six.print_(color + json.dumps(data, indent=4))
    six.print_(color + '=' * width)
