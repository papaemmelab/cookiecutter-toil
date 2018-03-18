#!/bin/bash

# Run tox inside the container.

if [ "$1" = "--skip-build" ]; then
    echo "skipping build..."
else
    echo "building image, to skip run with --skip-build..."
    docker build -q -t test-image .
fi

# see https://explainshell.com/explain?cmd=set+-euxo%20pipefail
set -euxo pipefail

# remove pytest cache
find . -name '*.pyc' -exec rm {} +
find . -name '__pycache__' -exec rm -rf {} +

# test image
echo "testing docker image..."
docker run --rm test-image --version
docker run --rm --entrypoint "" -v `pwd`:/test -w /test \
    test-image bash -c "pip install tox > /dev/null 2>&1 && tox"

# move container coverage paths to local, see .coveragerc [paths] and this comment:
# https://github.com/pytest-dev/pytest-cov/issues/146#issuecomment-272971136
echo "combining container coverage..."
command -v coverage > /dev/null 2>&1 || pip install coverage
mv .coverage .coverage.tmp
coverage combine --append

echo "tests finished..."
