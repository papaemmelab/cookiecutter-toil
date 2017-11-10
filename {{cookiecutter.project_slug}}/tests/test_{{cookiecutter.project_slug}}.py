"""Tests for {{cookiecutter.project_slug}}."""

# python
import pytest

# local
from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import cli


@pytest.fixture
def response():
    """
    Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 10


def test_fixture(response):
    """Sample test function with the pytest fixture as an argument."""
    assert response == 10


def test_cli(response):
    """Sample test for the main command."""
    assert cli.main() == "hello world"


def test_version():
    """Sample test for the __version__ variable."""
    assert __version__ == "0.1.0"
