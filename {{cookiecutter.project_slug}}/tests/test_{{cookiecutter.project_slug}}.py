"""Tests for {{cookiecutter.project_slug}}."""

# python
from os.path import abspath
from os.path import dirname
from os.path import join
import pytest
import subprocess

# local
from {{cookiecutter.project_slug}} import __version__

TEST_DIR = abspath(dirname(__file__))

ROOT_DIR = abspath(join(TEST_DIR, ".."))


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


def test_{{cookiecutter.project_slug}}(tmpdir):
    """Sample test for the main command."""
    message = "This is a test message for the Universe."

    # Build command.
    cmd = [
        "python2",
        join(ROOT_DIR, "{{cookiecutter.project_slug}}", "__main__.py"),
        join(str(tmpdir), "jobstore"),
        "--message", message
        ]

    # Call pipeline
    output = subprocess.check_output(cmd)

    # Assert custom message is echoed in master log.
    assert message in output


def test_version():
    """Sample test for the __version__ variable."""
    assert __version__ == "0.1.0"
