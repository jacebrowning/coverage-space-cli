from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("coveragespace")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "(local)"

CLI = "coveragespace"
API = "https://api.coverage.space"

VERSION = f"{CLI} v{__version__}"

del PackageNotFoundError
del version
