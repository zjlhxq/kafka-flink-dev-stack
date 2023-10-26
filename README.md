# kafka-flink-dev-stack
A mini kafka flink demo stack with avro as the serialization format based on https://github.com/garystafford/flink-kafka-demo/

# Getting started with the dev stack
1. Basic development env setup (Ubuntu guest os, docker engine, git, maven/gradle, ide, java, python3)
2. Bring up the mini dev stack with docker-compose (the stack should work both in x86-64 and ARM64(apple silicon chip))
   > docker-compose -f docker/flink-kafka-stack.yml up -d
3. Run the python data generator script to simulate data ingestion
   > cd streaming-data-generator/sales_generator
   > python3 ./producer.py
5. Build the Kafka-Flink-demo job with cradle to generate fat/uber jar to be deployed to the Flink cluster
   > cd flink-kafka-demo
   > ./gradlew clean shadowJar
7. Deploy Flink jobs via shell scripts
   > ./deploy.sh
8. Submit flink jobs
   > ./submit-join-streams-job.sh
   > ./submit-running-totals-job.sh

# Checking the running status
1. Go to http://localhost:9080 to check the running status of the single-node kafka cluster
2. Go to http://localhost:9081 to check the running status of the flink cluster

# The architecture overview
The stack consists of a single-node Kafka cluster with KRaft(without ZooKeeper), a schema registry service instance, a Flink Job Manager instance, a Flink Task Manager instance, and a Kafka UI service
![mini-kafka-flink-stack](https://github.com/zjlhxq/kafka-flink-dev-stack/assets/8728130/b4725412-50bd-4d0e-85d3-f5bc542606fd)

The serialization format used is ‘AVRO’

The use case is to about joining two data streams by productId that come out of Kafka and sending the enriched messages to another Kafka topic 
