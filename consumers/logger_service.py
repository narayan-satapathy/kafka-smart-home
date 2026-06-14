from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "smart-home-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="logger-service",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Logger Service Running...")

for msg in consumer:
    event = msg.value
    print("LOG:", event)
