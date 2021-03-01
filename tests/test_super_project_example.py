"""Tests for `super_project_example` module."""
from typing import Generator

import pytest

import super_project_example


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield super_project_example.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.2.0"
