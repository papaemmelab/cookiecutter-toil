"""Tests for {{cookiecutter.project_slug}}."""
{% if cookiecutter.pipeline_type == "click" %}
from click.testing import CliRunner

{% endif %}
{% if cookiecutter.pipeline_type == "toil" %}
from os.path import join
import subprocess
{% endif %}
import pytest

from {{cookiecutter.project_slug}} import __version__
{% if cookiecutter.pipeline_type == "click" %}
from {{cookiecutter.project_slug}} import cli
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

{% if cookiecutter.pipeline_type == "toil" %}
def test_{{cookiecutter.project_slug}}(tmpdir):
    """Sample test for the main command."""
    message = "This is a test message for the Universe."

    # Build command.
    cmd = [
        "python2", "-m", "{{cookiecutter.project_slug}}",
        join(str(tmpdir), "jobstore"), "--message", message
        ]

    # Call pipeline
    output = subprocess.check_output(cmd)

    # Assert custom message is echoed in master log.
    assert message in output
{% elif cookiecutter.pipeline_type == "click" %}
def test_{{cookiecutter.project_slug}}():
    """Sample test for the main command."""
    message = "This is a test message for the Universe."
    runner = CliRunner()
    params = ["message", message]
    result = runner.invoke(cli.main, params)
    assert message in result.output
{% endif %}