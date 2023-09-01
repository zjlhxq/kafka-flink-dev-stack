#!/bin/bash

source ./env.sh
docker exec  ${FLINK_CONTAINER} flink run -c org.example.JoinStreams /tmp/flink-kafka-demo-1.2.0-all.jar
