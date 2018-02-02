"""
Based on the implementation of:
https://github.com/vgteam/toil--bindg/blob/master/src/toil_vg/singularity.py

Module for running Singularity (and Docker) images with Singularity. Derived
from https://github.com/BD2KGenomics/toil/blob/master/src/toil/lib/docker.py
with which nearly all code is shared, save the command lines used to run the
containers.

Docker images can be run by prefacing the input image with docker://
In this case, Singularity will download, convert, and cache the image on the
fly. This cache can be set with SINGULARITY_CACHEDIR, and defaults to the
user's home directory. This cache can be a major bottleneck when repeatedly
more different images than it can hold (not very many). So for this type of
usage pattern (concurrent or short consecutive calls to different images),
it is best to run Singularity images natively.
"""
import logging
import subprocess

_LOGGER = logging.getLogger(__name__)


def singularity_call(
        image,
        parameters=None,
        singularity_parameters=None,
        outfile=None,
        errfile=None,
        check_output=False):
    """
    Execute parameters in a singularity container via subprocess.

    The resulting command is in the format:

        singularity -q exec
            <list-of-singularity-params>
            <singularity-image>
            <list-of-cmd-params-executed-inside-container>

    Arguments:
        image (str): name of the singularity image.
        parameters (list): list of command line arguments passed to the image.
        singularity_parameters (list): parameteres to be pass to singularity.
        check_output (bool): when True, return singularity's output.
        outfile (str): pipe output of Docker call to file handle.
        errfile (str): pipe standard error of Docker call to file handle.

    Raises:
        CalledProcessorError: if the Singularity invocation returns a
        non-zero exit code. This function blocks until the subprocess call
        to Singularity returns.

    Returns:
        str: stdout from the singularity call.
    """
    # Setup the outgoing subprocess call for singularity
    command = ['singularity', '-q', 'exec']
    command += singularity_parameters or []
    command += [image]
    command += parameters or []

    subprocess_kwargs = {}
    if outfile:
        subprocess_kwargs['stdout'] = outfile
    if errfile:
        subprocess_kwargs['stderr'] = errfile

    if check_output:
        call_method = subprocess.check_output
    else:
        call_method = subprocess.check_call

    _LOGGER.info("Calling singularity with %s", repr(command))
    out = call_method(command, **subprocess_kwargs)
    return out
