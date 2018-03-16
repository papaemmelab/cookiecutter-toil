"""{{cookiecutter.project_slug}} cli tests."""
{% if cookiecutter.cli_type == "toil" %}
from os.path import join

import pytest

from {{cookiecutter.project_slug}} import cli


def test_main():
    """Sample test for main command."""
    with pytest.raises(SystemExit) as _:
        cli.main()
{% elif cookiecutter.cli_type == "click" %}
from click.testing import CliRunner
import pytest

from {{cookiecutter.project_slug}} import cli

def test_main():
    """Sample test for main command."""
    message = "This is a test message for the Universe."
    runner = CliRunner()
    params = ["message", message]
    result = runner.invoke(cli.main, params)
    assert message in result.output
{% endif %}
