#! /bin/bash

# switch to a new temporary branch
cd ..
mkdir build_dir
cd build_dir
git clone https://github.com/benkeser/info550
cd info550 
export TRAVIS_BUILD_DIR=$(pwd)

# run website/_build.sh 
website/_build.sh

# run website/_deploy.sh local
website/_deploy.sh local

# rm info550/info550 dir
cd $TRAVIS_BUILD_DIR/..
rm -rf build_dir
