#!/bin/bash

# generate avro schema json files with avdl file
# The avro-tools can be downloaded at: https://downloads.apache.org/avro/stable/java/avro-tools-1.11.2.jar
java -jar ./avro-tools-1.11.2.jar idl2schemata message-schema/src/main/avro/example.avdl ./streaming-sales-generator/sales_generator/avro/