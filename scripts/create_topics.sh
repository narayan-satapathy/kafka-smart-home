#!/bin/bash

set -e

echo "Creating topic: smart-home-events"

docker compose exec kafka \
kafka-topics \
--create \
--if-not-exists \
--topic smart-home-events \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1

echo ""
echo "Topics list:"

docker compose exec kafka \
kafka-topics \
--list \
--bootstrap-server localhost:9092