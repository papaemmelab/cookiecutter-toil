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
        "project_slug": "test_project"
        }


@pytest.fixture
def recreate(request):
    """See conftest.py for definition of custom --recreate option."""
    return request.config.getoption("--recreate", False)


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
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


def run_tox(cli_type, cookies, context, recreate):
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

    # Check if environments should be rebuilt.
    if recreate:
        cmd.append("--recreate")

    # Call tox!
    subprocess.check_call(cmd, cwd=result.project.strpath)


def test_toil_tox(cookies, context, recreate):
    """Generated toil project should pass tests"""
    run_tox(
        cli_type="toil",
        context=context,
        recreate=recreate,
        cookies=cookies,
        )


def test_click_tox(cookies, context, recreate):
    """Generated click project should pass tests"""
    run_tox(
        cli_type="click",
        context=context,
        recreate=recreate,
        cookies=cookies,
        )
