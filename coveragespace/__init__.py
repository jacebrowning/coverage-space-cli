"""Package for coverage.space CLI."""

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('coverage-space').version
except DistributionNotFound:
    __version__ = '(local)'

CLI = 'coverage.space'
API = 'https://api.coverage.space'

VERSION = "{0} v{1}".format(CLI, __version__)
