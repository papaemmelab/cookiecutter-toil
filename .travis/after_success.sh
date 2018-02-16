if which python2 > /dev/null 2>&1;
then
    cookiecutter $TRAVIS_BUILD_DIR -o /tmp/ --no-input
    cd /tmp/test_project && tox --workdir $TRAVIS_BUILD_DIR/.tox/toil/
    cd /tmp/test_project && codecov --disable search -F toilcov
else
    echo "python2 not available, skipping codecov..."
fi
