#! /bin/bash

# switch to a new temporary branch
mkdir build_dir
cd build_dir
export TRAVIS_BUILD_DIR=$(pwd)
git clone https://github.com/benkeser/info550 

mkdir info550
git clone -b gh-pages \
  https://github.com/benkeser/info550 \
  info550

git checkout -b temporary

# run website/_build.sh 
website/_build.sh

# run website/_deploy.sh local
website/_deploy.sh

# rm info550/info550 dir
cd TRAVIS_BUILD_DIR/..
rm -rf build_dir
