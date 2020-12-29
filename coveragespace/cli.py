"""Update project metrics on The Coverage Space.

Usage:
  coveragespace set <metric> [<value>] [--verbose] [--exit-code]
  coveragespace reset [--verbose]
  coveragespace view [--verbose]
  coveragespace (-h | --help)
  coveragespace (-V | --version)

Options:
  -h --help         Show this help screen.
  -V --version      Show the program version.
  -v --verbose      Always display the coverage metrics.
  -x --exit-code    Return non-zero exit code on failures.

"""

import json
import sys
from shutil import get_terminal_size

import colorama
import log
from docopt import docopt

from . import API, VERSION, client, coverage, repository, services


def main():
    """Parse command-line arguments, configure logging, and run the program."""
    colorama.init(autoreset=True)
    arguments = docopt(__doc__, version=VERSION)
    log.init(level=log.DEBUG if arguments["--verbose"] else log.WARNING)

    if services.detected():
        log.info("Coverage check skipped when running on CI service")
        sys.exit()

    if arguments["view"]:
        success = view()
    else:
        slug = repository.get_slug()
        success = call(
            slug,
            arguments["<metric>"],
            arguments["<value>"],
            arguments["reset"],
            arguments["--verbose"],
            arguments["--exit-code"],
        )

    if not success and arguments["--exit-code"]:
        sys.exit(1)


def call(slug, metric, value, reset=False, verbose=False, hardfail=False):
    """Call the API and display errors."""
    url = "{}/{}".format(API, slug)
    if reset:
        data = {metric: None}
        response = client.delete(url, data)
    else:
        data = {metric: value or coverage.get_coverage()}
        response = client.get(url, data)

    if response.status_code == 200:
        if verbose:
            display("coverage increased", response.json(), colorama.Fore.GREEN)
        return True

    if response.status_code == 202:
        display("coverage reset", response.json(), colorama.Fore.BLUE)
        return True

    if response.status_code == 422:
        color = colorama.Fore.RED if hardfail else colorama.Fore.YELLOW
        data = response.json()
        data["help"] = "To reset metrics, run: ^coveragespace reset$"  # type: ignore
        display("coverage decreased", data, color)
        coverage.launch_report()
        return False

    try:
        data = response.json()
        display("coverage unknown", data, colorama.Fore.RED)
    except (TypeError, ValueError) as exc:
        data = response.data.decode("utf-8")
        log.error("%s\n\nwhen decoding response:\n\n%s\n", exc, data)
    return False


def display(title, data, color=""):
    """Write colored text to the console."""
    color += colorama.Style.BRIGHT
    width, _ = get_terminal_size()
    print(color + "{0:=^{1}}".format(" " + title + " ", width))
    message = json.dumps(data, indent=4)
    message = message.replace("^", colorama.Fore.WHITE + colorama.Style.BRIGHT)
    message = message.replace("$", colorama.Style.RESET_ALL)
    print(message)
    print(color + "=" * width)


def view():
    """View the local coverage report."""
    coverage.launch_report(always=True)
    return True
