#!/bin/bash

# Runs the Flink SQL Client script
  # Starts the SQL Client in embedded mode (does not connect to an external Flink cluster)
  # Specifies a directory to load additional libraries (JAR files)
q


${FLINK_HOME}/bin/sql-client.sh embedded -l ${SQL_CLIENT_HOME}/lib
