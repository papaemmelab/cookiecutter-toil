"""{{cookiecutter.project_slug}} validators."""

from glob import glob
import os

from {{cookiecutter.project_slug}} import exceptions


def validate_patterns_are_files(patterns, check_size=True):
    """
    Check that a list of `patterns` are valid files.

    Arguments:
        patterns (list): a list of patterns to be check.
        check_size (bool): check size is not zero for all files matched.

    Returns:
        bool: True if all patterns match existing files.
    """
    for pattern in patterns:
        files = list(glob(pattern))

        if not files:
            msg = f"{pattern} pattern matched no files."
            raise exceptions.ValidationError(msg)

        for i in files:
            if not os.path.isfile(i):
                msg = f"{i} is not a file."
                raise exceptions.ValidationError(msg)

            if check_size and not os.path.getsize(i) > 0:
                msg = f"{i} is an empty file."
                raise exceptions.ValidationError(msg)

    return True


def validate_patterns_are_dirs(patterns):
    """
    Check that a list of `patterns` are valid dirs.

    Arguments:
        patterns (list): a list of directory patterns.

    Returns:
        bool: True if all patterns match existing directories.
    """
    for pattern in patterns:
        dirs = list(glob(pattern))

        if not dirs:
            msg = f"{pattern} pattern matched no dirs."
            raise exceptions.ValidationError(msg)

        for i in dirs:
            if not os.path.isdir(i):
                msg = f"{i} is not a directory."
                raise exceptions.ValidationError(msg)

    return True
