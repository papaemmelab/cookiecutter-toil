"""{{cookiecutter.project_slug}} specific excemptions."""


class ValidationError(Exception):

    """A class to raise when a validation error occurs."""


class MissingRequirementError(Exception):

    """A class to raise when a requirement is missing."""


class MissingOutputError(Exception):

    """A class to raise when a file that should exist is missing."""


class ConfigurationError(Exception):

    """A class to raise when leuktools is not properly configured."""


class CantBeRunError(Exception):

    """A class to raise when a pipeline just cannot be run."""


class MissingDataError(Exception):

    """A class to raise when data is missing."""
