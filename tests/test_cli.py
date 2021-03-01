"""Tests for `super_project_example`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import super_project_example
from super_project_example import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "super_project_example.cli.main"),
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { super_project_example.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, options)
    assert result.exit_code == 0
    assert expected in result.output
