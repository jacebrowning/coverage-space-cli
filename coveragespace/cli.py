"""Update project metrics on The Coverage Space.

Usage:
  coverage.space <owner/repo> <metric> [<value>] [--verbose] [--exit-code]
  coverage.space (-h | --help)
  coverage.space (-V | --version)

Options:
  -h --help         Show this help screen.
  -V --version      Show the program version.
  -v --verbose      Always display the coverage metrics.
  -x --exit-code    Return non-zero exit code on failures.

"""

from __future__ import unicode_literals

import sys
import time
import json
import logging

import six
from docopt import docopt
import requests
import colorama
from backports.shutil_get_terminal_size import get_terminal_size

from . import API, VERSION

from .plugins import get_coverage
from .cache import Cache


log = logging.getLogger(__name__)
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

    if verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(levelname)s: %(name)s: %(message)s",
        )

    success = call(slug, metric, value, verbose, hardfail)

    if not success and hardfail:
        sys.exit(1)


def call(slug, metric, value, verbose=False, hardfail=False):
    """Call the API and display errors."""
    url = "{}/{}".format(API, slug)
    data = {metric: value}
    response = request(url, data)

    if response.status_code == 200:
        if verbose:
            display("coverage increased", response.json(), colorama.Fore.GREEN)
        return True

    elif response.status_code == 422:
        color = colorama.Fore.RED if hardfail else colorama.Fore.YELLOW
        display("coverage decreased", response.json(), color)
        return False

    else:
        try:
            data = response.json()
            display("coverage unknown", data, colorama.Fore.RED)
        except (TypeError, ValueError) as exc:
            data = response.data.decode('utf-8')
            log.error("%s\n\nwhen decoding response:\n\n%s\n", exc, data)
        return False


def request(url, data):
    """Make request to external API."""
    log.info("Updating %s: %s", url, data)

    response = cache.get(url, data)
    if response is None:
        for _ in range(3):
            response = requests.put(url, data=data)
            if response.status_code == 500:
                time.sleep(3)
                continue
            else:
                break
        cache.set(url, data, response)

    log.info("Response: %s", response)

    return response


def display(title, data, color=""):
    """Write colored text to the console."""
    color += colorama.Style.BRIGHT
    width, _ = get_terminal_size()
    six.print_(color + "{0:=^{1}}".format(' ' + title + ' ', width))
    six.print_(color + json.dumps(data, indent=4))
    six.print_(color + '=' * width)
