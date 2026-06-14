from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "smart-home-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="demo-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("listening...")

for msg in consumer:
    print("received:", msg.value)
