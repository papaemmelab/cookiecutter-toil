DEPLOY_REPO_URL=https://${GH_TOKEN}@github.com/leukgen/toil_example.git
DEPLOY_BASE_DIR=/tmp/toil_example_deploy
DEPLOY_REPO_DIR=/tmp/toil_example_deploy/toil_example
DEPLOY_REPO_BRA=${TRAVIS_PULL_REQUEST_BRANCH:="$TRAVIS_BRANCH"}

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

if [ "$DEPLOY_TOIL_EXAMPLE" = "true" ];
then
    mkdir $DEPLOY_BASE_DIR && cd $DEPLOY_BASE_DIR
    git clone $DEPLOY_REPO_URL $DEPLOY_REPO_DIR

    echo "checking out to current branch: $DEPLOY_REPO_BRA"
    cd $DEPLOY_REPO_DIR && git checkout -b $DEPLOY_REPO_BRA

    echo "temporarily moving git directory out of repo..."
    mv $DEPLOY_REPO_DIR/.git $DEPLOY_BASE_DIR

    echo "force creating cookiecutter..."
    cd $DEPLOY_BASE_DIR
    cookiecutter $TRAVIS_BUILD_DIR --no-input -f -o $DEPLOY_BASE_DIR

    echo "moving back .git directory to repo..."
    mv $DEPLOY_BASE_DIR/.git $DEPLOY_REPO_DIR
    cd $DEPLOY_REPO_DIR && git add .

    echo "pushing changes: 🤖 travis build $TRAVIS_BUILD_NUMBER..."
    git commit --message "🤖 travis build $TRAVIS_BUILD_NUMBER"
    git push -u origin $DEPLOY_REPO_BRA
else
    echo "DEPLOY_TOIL_EXAMPLE not set to true, skipping..."
fi
