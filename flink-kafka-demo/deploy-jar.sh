#!/bin/bash


source env.sh

docker cp build/libs/flink-kafka-demo-1.2.0-all.jar ${FLINK_CONTAINER}:/tmp
#docker cp build/install/flink-kafka-demo-shadow/lib/flink-kafka-demo-1.2.0-all.jar ${FLINK_CONTAINER}:/tmp
#docker cp ../message-schema/build/libs/message-schema-all.jar  ${FLINK_CONTAINER}:/opt/flink/lib
#docker exec -it ${FLINK_CONTAINER} bash
