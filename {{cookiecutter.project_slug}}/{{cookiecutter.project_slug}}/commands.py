"""{{cookiecutter.project_slug}} commands."""

import subprocess

from toil_container import ContainerCallJob
from toil_container import ContainerShortArgumentParser

from {{cookiecutter.project_slug}} import __version__


class BaseJob(ContainerCallJob):

    """
    A job base class that inherits from `ContainerCallJob`.

    This class provides, abstract methods `check_call` and `check_output` which
    will use `docker`, `singularity` or `subprocess` to execute system calls.

    Arguments:
        options (argparse.Namespace): an `argparse.Namespace` with pipeline
            options obtained with `ContainerShortArgumentParser`.

    Attributes:
        options (argparse.Namespace): `options` is set as an object attribute.
    """

    SHARED_VARIABLE = "Hello World"


class Hello(BaseJob):

    """A simple job to log the SHARED_VARIABLE to master."""

    def run(self, fileStore):
        """Say hello to the world."""
        fileStore.logToMaster(self.SHARED_VARIABLE)


class HelloMessage(BaseJob):

    """A simple job to log a custom message to master."""

    def run(self, fileStore):
        """Run `echo` with docker, singularity or subprocess."""
        output = self.check_output(["echo", self.options.message])
        fileStore.logToMaster(output)


def run_toil(options):
    """Toil implementation for {{cookiecutter.project_slug}}."""
    head = Hello(cores=4, memory="12G", options=options)
    child = HelloMessage(cores=4, memory="12G", options=options)
    head.addChild(child)
    ContainerCallJob.Runner.startToil(head, options)


def get_parser():
    """Get pipeline configuration using toil's."""
    parser = ContainerShortArgumentParser(
        version=__version__,
        description="{{cookiecutter.project_slug}} pipeline",
        )

    settings = parser.add_argument_group("{{cookiecutter.project_slug}} arguments")

    settings.add_argument(
        "--message",
        help="a message to be echoed to the Universe",
        required=False,
        default="hello Universe, this text is used in the pipeline tests",
        )

    settings.add_argument(
        "--total",
        help="total times message should be printed",
        required=False,
        default=1,
        type=int,
        )

    return parser


def process_parsed_options(options):
    """Perform validations and add post parsing attributes to `options`."""
    if options.writeLogs is not None:
        subprocess.check_call(["mkdir", "-p", options.writeLogs])

    # an example of how to post process variables after parsing
    options.message = options.message * options.total

    return options


def main():
    """
    Parse options and run toil.

    **Workflow**

    1. Define Options `get_parser`: build an `arg_parse` object that
       includes both toil options and pipeline specific options. These will be
       separated in different sections of the `--help` text and used by the
       jobs to do the work.

    2. Validate with `process_parsed_options`: once the options are parsed, it
       maybe necessary to conduct *post-parsing* operations such as adding new
       attributes to the `options` namespace or validating combined arguments.

    3. Execute with `run_toil`: this function uses the `options` namespace to
       build and run the toil `DAG`.
    """
    options = get_parser().parse_args()
    options = process_parsed_options(options=options)
    run_toil(options=options)


if __name__ == "__main__":
    main()
