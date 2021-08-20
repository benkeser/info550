#! /bin/bash

# switch to a new temporary branch
git checkout -b temporary

# set TRAVIS_BUILD_DIR as current directory
export TRAVIS_BUILD_DIR=$(pwd)

# run website/_build.sh 
website/_build.sh

# run website/_deploy.sh local
# rm info550/info550 dir 
# checkout master
# delete temporary branch