#!/bin/bash

mvn clean compile assembly:single
docker cp ./target/flink-test-1.0-SNAPSHOT-jar-with-dependencies.jar \
  jobmanager-name:/opt/flink/flink-test-1.0-SNAPSHOT-jar-with-dependencies.jar