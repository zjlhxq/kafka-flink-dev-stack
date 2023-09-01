#!/bin/bash

export FLINK_CONTAINER=$(docker container ls --filter  name=docker_jobmanager_1 --format "{{.ID}}")

