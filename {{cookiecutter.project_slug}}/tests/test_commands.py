"""={{cookiecutter.project_slug}} commands tests."""

from os.path import join

import pytest

from {{cookiecutter.project_slug}} import commands


def test_run_toil(tmpdir):
    """Sample test for the main command."""
    #  Define arguments.
    message = "This is a test message for the Universe."
    logfile = tmpdir.join("log.txt")
    jobstore = tmpdir.join("jobstore")
    total = 3
    args = [
        jobstore.strpath,
        "--message", message,
        "--total", str(total),
        "--logFile", logfile.strpath,
        ]

    # Get and validate options.
    parser = commands.get_parser()
    options = parser.parse_args(args)
    options = commands.process_parsed_options(options)

    # Call pipeline
    commands.run_toil(options)

    # Assert custom message is echoed in master log.
    with open(logfile.strpath) as f:
        assert len(f.read().split(message)) == total + 1
