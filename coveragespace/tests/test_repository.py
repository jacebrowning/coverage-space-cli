# pylint: disable=unused-variable,unused-argument,expression-not-assigned,singleton-comparison,redefined-outer-name

import os

import pytest

from ..repository import get_slug


@pytest.fixture
def git_config(tmp_path):
    os.chdir(tmp_path)
    config = tmp_path / ".git" / "config"
    config.parent.mkdir()
    config.write_text(
        """
        [remote "origin"]
            url = https://github.com/owner/project.git
        """
    )
    return config


@pytest.fixture
def unknown_data(tmp_path):
    os.chdir(tmp_path)


def describe_get_slug():
    def it_supports_git(expect, git_config):
        expect(get_slug()) == "owner/project"

    def it_handles_missing_remote(expect, git_config):
        git_config.write_text(
            """
            [branch "main"]
	            remote = https://github.com/owner/project.git
            """
        )
        expect(get_slug()) == "owner/project"

    def it_handles_duplicate_options_in_git_config(expect, git_config):
        git_config.write_text(
            """
            [remote "origin"]
                url = https://github.com/owner/project.git
            [branch "main"]
                remote = origin
                merge = refs/heads/main
                vscode-merge-base = abc123
                vscode-merge-base = def456
            """
        )
        expect(get_slug()) == "owner/project"

    def it_raise_an_exception_when_no_match(expect, unknown_data):
        with expect.raises(RuntimeError):
            get_slug()
