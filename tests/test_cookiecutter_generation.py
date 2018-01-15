"""Tests were inspired by https://github.com/pydanny/cookiecutter-django."""

import os
import re
import subprocess

from binaryornot.check import is_binary
import pytest

PATTERN = "{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "full_name": "John Smith",
        "email": "smithj@mskcc.org",
        "github_account": "leukgen",
        "project_slug": "test_project"
        }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
        ]


def check_paths(paths):
    """
    Method to check all paths have correct substitutions.
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, "r"):
            match = RE_OBJ.search(line)
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


def test_toil(cookies, context):
    """Generated toil project should pass tests"""
    context["cli_type"] = "toil"
    result = cookies.bake(extra_context=context)
    subprocess.check_call(["py.test", "-s", "tests"], cwd=str(result.project))

    # Test pylint of generated project.
    pylintrc = os.path.join(str(result.project), ".pylintrc")
    root = os.path.join(str(result.project), context["project_slug"])
    subprocess.check_call(["pylint", "--rcfile=" + pylintrc, root])


def test_click(cookies, context):
    """Generated click project should pass tests"""
    context["cli_type"] = "click"
    result = cookies.bake(extra_context=context)
    subprocess.check_call(["py.test", "-s", "tests"], cwd=str(result.project))

    # Test pylint of generated project.
    pylintrc = os.path.join(str(result.project), ".pylintrc")
    root = os.path.join(str(result.project), context["project_slug"])
    subprocess.check_call(["pylint", "--rcfile=" + pylintrc, root])


@pytest.mark.skipif(
    os.getenv("TEST_TOIL_TOX") != "yes",
    reason="export TEST_TOIL_TOX=yes to run tox for toil.")
def test_toil_tox(cookies, context):
    """Generated toil project should pass tests"""
    context["cli_type"] = "toil"
    result = cookies.bake(extra_context=context)
    subprocess.check_call(["tox"], cwd=str(result.project))


@pytest.mark.skipif(
    os.getenv("TEST_CLICK_TOX") != "yes",
    reason="export TEST_CLICK_TOX=yes to run tox for toil.")
def test_click_tox(cookies, context):
    """Generated click project should pass tests"""
    context["cli_type"] = "click"
    result = cookies.bake(extra_context=context)
    subprocess.check_call(["tox"], cwd=str(result.project))
