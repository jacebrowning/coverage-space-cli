# Metrics Reset

If code coverage metrics have decreased, but you would like to silence the warning and reset metrics to the next received value:

```sh
$ coverage.space <owner/repo> --reset
```

# Verbosity

To always display the coverage results, use the `--verbose` option:

```sh
$ coverage.space <owner/repo> <metric> --verbose
```

# Exit Codes

To return a non-zero exit code when coverage decreases, use the `--exit-code` option:

```sh
$ coverage.space <owner/repo> <metric> --exit-code
```
