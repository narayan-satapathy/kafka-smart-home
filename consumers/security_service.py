from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "smart-home-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="security-service",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Security Service Running...")

for msg in consumer:
    event = msg.value

    if event["type"] == "motion" and event["value"] is True:
        print("🚨 INTRUSION ALERT:", event)
