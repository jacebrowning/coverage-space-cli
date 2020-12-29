# Advanced Usage

The client can also be used to view and reset coverage metrics.

## Viewing Reports

To update the overall coverage metric and view the local coverage report:

```text
$ coveragespace
```

or to simply view the current report:

```text
$ coveragespace view
```

## Resetting Metrics

If code coverage metrics have decreased, but you would like to silence the warning and reset metrics to the next received value:

```text
$ coveragespace reset
```

## Increasing Verbosity

To always display the coverage results, use the `--verbose` option:

```text
$ coveragespace set <metric> --verbose
```

## Exit Codes

To return a non-zero exit code when coverage decreases, use the `--exit-code` option:

```text
$ coveragespace set <metric> --exit-code
```
