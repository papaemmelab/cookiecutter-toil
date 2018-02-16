"""Tests were inspired by https://github.com/pydanny/cookiecutter-django."""

from os.path import join
from os.path import abspath
from os.path import dirname
import os
import re
import subprocess

import pytest
from binaryornot.check import is_binary

ROOT = abspath(join(dirname(__file__), ".."))


@pytest.fixture
def context():
    return {
        "full_name": "John Smith",
        "email": "smithj@mskcc.org",
        "github_account": "leukgen",
        "project_slug": "test_project",
        "project_description": "An awesome python package to be tested.",
        }


@pytest.fixture
def recreate(request):
    """See conftest.py for definition of custom --tox-recreate option."""
    return request.config.getoption("--tox-recreate", False)


@pytest.fixture
def develop(request):
    """See conftest.py for definition of custom --tox-develop option."""
    return request.config.getoption("--tox-develop", False)


@pytest.fixture
def pytest_args(request):
    """See conftest.py for definition of custom --tox--pytest-args option."""
    return request.config.getoption("--tox-pytest-args", None)


@pytest.fixture
def envlist(request):
    """See conftest.py for definition of custom --tox--envlist option."""
    return request.config.getoption("--tox-envlist", None)


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
        ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    pattern = "{{(\s?cookiecutter)[.](.*?)}}"
    regex = re.compile(pattern)
    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, "r"):
            match = regex.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


def tox(cli_type, cookies, context, recreate, develop, pytest_args, envlist):
    """Run tox tests given for click or toil."""
    if cli_type not in {"click", "toil"}:
        raise Exception("cli_type is not click or toil: %s" % cli_type)

    # Make sure tox directory exists.
    toxdir = join(ROOT, ".tox")
    if not os.path.isdir(toxdir):
        os.makedirs(toxdir)

    workdir = join(ROOT, ".tox", cli_type)
    context["cli_type"] = cli_type
    result = cookies.bake(extra_context=context)
    cmd = ["tox", "--workdir", workdir]
    env = os.environ

    # Check if environments should be rebuilt.
    if recreate:
        cmd.append("--recreate")

    if develop:
        cmd.append("--develop")

    if envlist:
        cmd += ["-e", envlist]

    if pytest_args:
        env["TOX_PYTEST_ARGS"] = pytest_args

    # Call tox!
    subprocess.check_call(cmd, env=env, cwd=result.project.strpath)


@pytest.mark.skipif(
    os.getenv("SKIP_TOIL_TEST", "false").lower() == "true",
    reason="set SKIP_TOIL_TEST=true to test the toil mode."
)
def test_toil_tox(cookies, context, recreate, develop, pytest_args, envlist):
    """Test that generated toil project pass tests."""
    tox(
        cli_type="toil",
        context=context,
        recreate=recreate,
        cookies=cookies,
        develop=develop,
        pytest_args=pytest_args,
        envlist=envlist,
        )


def test_click_tox(cookies, context, recreate, develop, pytest_args, envlist):
    """Test that generated click project pass tests."""
    tox(
        cli_type="click",
        context=context,
        recreate=recreate,
        cookies=cookies,
        develop=develop,
        pytest_args=pytest_args,
        envlist=envlist,
        )
