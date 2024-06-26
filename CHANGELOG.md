# Revision History

## 6.1 (2024-04-04)

- Added a `report` link when coverage decreases.

## 6.0.2 (2022-11-13)

- Fixed handling of Git directories lacking an origin.

## 6.0.1 (2022-11-23)

- Loosened the `minilog` dependency.

## 6.0 (2022-09-18)

- Dropped support for Python 3.7.

## 5.0 (2022-08-14)

- Dropped support for Python 3.6.

## 4.2 (2021-06-05)

- Updated the CoveragePy plugin to walk the filesystem in search of `htmlcov/index.html`.

## 4.1 (2021-02-21)

- Updated CLI help text to suggest invoking by Poetry when appropriate.

## 4.0 (2020-12-31)

- **BREAKING:** Removed `<owner/repo>` CLI argument in favor of automatic detection.
- Updated the default CLI command to display metrics and launch the report.

## 3.1.1 (2020-02-01)

- Fixed caching to clear after resetting metrics.

## 3.1 (2020-01-27)

- Added highlight to the reset command.
- Dropped support for Python 3.5.
- Fixed caching of API requests.

## 3.0.1 (2020-01-01)

- Dropped version requirement for `coverage` dependency.

## 3.0 (2019-11-27)

- Dropped support for Python 2.

## 2.1 (2018-10-27)

- Added support for custom `coverage.py` data locations.

## 2.0 (2018-09-08)

- **BREAKING:** Renamed PyPI project to `coveragespace`.
- Added `DRONE` to the list of service environment variables.

## 1.0.2 (2018/05/16)

- Brocaded dependency on `coverage` and `requests` to accept any version.

## 1.0.1 (2018/05/15)

- Broadened dependency on `six` to `1.x`.

## 1.0 (2018-03-15)

- **BREAKING:** Renamed PyPI project to `coverage-space`.

## 0.8 (2017-04-16)

- Added slash requirement to `<owner/repo>` slug argument.
- Added automatic coverage report launching when coverage decreases.

## 0.7.2 (2017-03-11)

- Allow coverage to be disabled with `DISABLE_COVERAGE`.

## 0.7.1 (2017-03-11)

- Delayed coverage loading until needed to allow faster exits.

## 0.7 (2017-01-31)

- Added `--reset` command to reset all coverage metrics.

## 0.6.3 (2016-09-30)

- Fixed dependency on `coverage`.

## 0.6.2 (2016-09-29)

- Updated API call to use SSL.

## 0.6.1 (2016-09-16)

- Added no-op when running on CI services.

## 0.6 (2016-09-12)

- Added no-op when running on CI services.

## 0.5 (2016-09-09)

- Added logging to debug errors with the `--version` option.
- Added retry logic in cases where the API returns server errors.

## 0.4 (2016-08-22)

- Added client-side caching to reduce network traffic.
- Added an option to always display coverage metrics.

## 0.3.1 (2016-08-19)

- Fixed terminal width detection.

## 0.3 (2016-07-30)

- Added Windows support.

## 0.2 (2016-04-16)

- Added the option to return non-zero exit codes.

## 0.1.1 (2016-02-06)

- Added Python 2.7 support.

## 0.1 (2016-02-06)

- Initial release.
