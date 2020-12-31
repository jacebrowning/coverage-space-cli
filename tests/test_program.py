# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned


import os
import sys

import pytest
import scripttest
from expecter import expect


@pytest.fixture
def env(tmp_path):
    env = scripttest.TestFileEnvironment(tmp_path / "test")
    env.environ.pop("APPVEYOR", None)
    env.environ.pop("CI", None)
    env.environ.pop("CONTINUOUS_INTEGRATION", None)
    env.environ.pop("DISABLE_COVERAGE", None)
    env.environ.pop("TRAVIS", None)
    config = env.base_path / ".git" / "config"
    config.parent.mkdir()
    config.write_text(
        """
        [remote "origin"]
        url = http://example.com/jacebrowning/coverage-space-cli-demo
        """,
    )
    return env


@pytest.fixture
def env_reset(env):
    config = env.base_path / ".git" / "config"
    text = config.read_text()
    config.write_text(text.replace("demo", "demo-reset"))
    return env


def cli(env, *args):
    prog = os.path.join(os.path.dirname(sys.executable), "coveragespace")
    cmd = env.run(prog, *args, expect_error=True)
    print(cmd)
    return cmd


def describe_cli():
    def it_displays_metrics_and_launches_local_report(env):
        cmd = cli(env)

        expect(cmd.returncode) == 0
        expect(cmd.stderr) == ""
        expect(cmd.stdout).contains("coverage updated")

    def it_fails_with_unknown_arguments(env):
        cmd = cli(env, "foobar")

        expect(cmd.returncode) == 1
        expect(cmd.stderr).contains("Usage:")

    def describe_update():
        def it_can_update_metrics(env):
            cmd = cli(env, "update", "unit", "100")

            expect(cmd.returncode) == 0
            expect(cmd.stderr) == ""
            expect(cmd.stdout) == ""

        def it_indicates_when_metrics_decrease(env):
            cmd = cli(env, "update", "unit", "0")

            expect(cmd.returncode) == 0
            expect(cmd.stderr) == ""
            expect(cmd.stdout).contains("coverage decreased")
            expect(cmd.stdout).contains("To reset metrics, run: coveragespace reset")

        def it_fails_when_metrics_decrease_if_requested(env):
            cmd = cli(env, "update", "unit", "0", "--exit-code")

            expect(cmd.returncode) == 1
            expect(cmd.stderr) == ""
            expect(cmd.stdout).contains("coverage decreased")

        def it_always_display_metrics_when_verbose(env):
            cmd = cli(env, "update", "unit", "100", "--verbose")

            expect(cmd.returncode) == 0
            expect(cmd.stderr) != ""  # expect lots of logging
            expect(cmd.stdout).contains("coverage updated")

        def it_skips_when_running_on_ci(env):
            env.environ["CI"] = "true"

            cmd = cli(env, "update", "unit", "0", "--exit-code", "--verbose")

            expect(cmd.returncode) == 0
            expect(cmd.stderr).contains("Coverage check skipped")
            expect(cmd.stdout) == ""

    def describe_reset():
        def it_can_reset_metrics(env_reset):
            cmd = cli(env_reset, "reset")

            expect(cmd.returncode) == 0
            expect(cmd.stderr) == ""
            expect(cmd.stdout).contains("coverage reset")

    def describe_view():
        def it_launches_the_local_coverage_report(env):
            cmd = cli(env, "view")

            expect(cmd.returncode) == 0
            expect(cmd.stderr) == ""
            expect(cmd.stdout).contains("")
