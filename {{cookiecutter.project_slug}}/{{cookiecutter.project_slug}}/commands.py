"""{{cookiecutter.project_slug}} commands."""

import subprocess

from toil_container import ContainerArgumentParser
from toil_container import ContainerJob

from {{cookiecutter.project_slug}} import __version__


class Hello(ContainerJob):

    def run(self, fileStore):
        """
        Log value of `total` from the `options` attribute.

        `ContainerJob` loads the argument `options` as an object attribute.
        Learn more here https://github.com/papaemmelab/toil_container.
        """
        fileStore.logToMaster("The total is: %s" % self.options.total)


class HelloMessage(ContainerJob):

    def run(self, fileStore):
        """
        Run `echo` with docker, singularity or subprocess.

        Use `self.call` to run commands with docker, singularity or subprocess.
        Learn more here https://github.com/papaemmelab/toil_container.
        """
        output = self.call(["echo", self.options.message], check_output=True)
        fileStore.logToMaster(output)


def get_parser():
    """Get pipeline configuration using toil's."""
    parser = ContainerArgumentParser(
        version=__version__,
        description="A hello world toil pipeline.",
        )

    settings = parser.add_argument_group("pipeline arguments")

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


def run_toil(options):
    """Run toil pipeline give an options namespace."""
    head = Hello(cores=1, memory="1G", options=options)
    child = HelloMessage(cores=1, memory="1G", options=options)
    head.addChild(child)
    ContainerJob.Runner.startToil(head, options)


def main():
    """
    Parse options and run toil.

    **Workflow**

    1. Define Options using `get_parser`: build an `arg_parse` object that
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
