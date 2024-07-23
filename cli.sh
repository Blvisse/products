#!/bin/bash

function build(){
  docker rmi --force fastapi:v1.2

  docker build -t fastapi:v1.2 .
}

function docker_run() {
  docker run -d --rm --name fastapi fastapi:v1.2

}

function run_test() {
    docker exec fastapi sh -c "python3 -m pytest -vv"
}

echo "Welcome to the build"
build
echo "Currently running docker image"
docker_run
echo "Running tests"
run_test
