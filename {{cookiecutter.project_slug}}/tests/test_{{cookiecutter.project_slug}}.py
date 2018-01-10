"""Tests for {{cookiecutter.project_slug}}."""
{% if cookiecutter.cli_type == "toil" %}
from os.path import join
import pytest

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import commands


def test_{{cookiecutter.project_slug}}(tmpdir):
    """Sample test for the main command."""
    #  Define arguments.
    message = "This is a test message for the Universe."
    outfile = join(str(tmpdir), "hello.txt")
    jobstore = join(str(tmpdir), "jobstore")
    total = 3
    args = [
        jobstore,
        "--message", message,
        "--outfile", outfile,
        "--total", str(total),
        ]

    # Get and validate options.
    parser = commands.get_parser()
    options = parser.parse_args(args)
    options = commands.validate_options(options)

    # Call pipeline
    commands.run_toil(options)

    # Assert custom message is echoed in master log.
    with open(outfile) as f:
        assert len(f.read().split(message)) == total + 1
{% elif cookiecutter.cli_type == "click" %}
from click.testing import CliRunner

import pytest

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import cli

def test_{{cookiecutter.project_slug}}():
    """Sample test for the main command."""
    message = "This is a test message for the Universe."
    runner = CliRunner()
    params = ["message", message]
    result = runner.invoke(cli.main, params)
    assert message in result.output
{% endif %}

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


def test_version():
    """Sample test for the __version__ variable."""
    assert __version__ == "0.1.0"
