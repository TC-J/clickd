import pytest

from .cli import cli_test

from click.testing import CliRunner


@pytest.fixture
def runner() ->CliRunner:
    return CliRunner()


def test_clickd_toplevel_subcmd(runner):
    result = runner.invoke(cli_test, ["b"])

    assert result.exit_code == 0

    assert result.output == "b\n"


def test_clickd_subgrp_subcomd(runner):
    result = runner.invoke(cli_test, ["a", "v"])

    assert result.exit_code == 0

    assert result.output == "v\n"


def test_clickd_subgrp_subcmd_w_arg_and_opt(runner):
    result = runner.invoke(cli_test, ["e", "f", "hello", "--double"])

    assert result.exit_code == 0

    assert result.output == "hello\nhello\n"


def test_clickd_multinested_subcmd(runner):
    result = runner.invoke(cli_test, ["e", "g", "j", "123"])

    assert result.exit_code == 0

    assert result.output == "123\n"

    result = runner.invoke(cli_test, ["e", "h", "k"])

    assert result.exit_code == 0

    assert result.output == "k\n"