from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "smart-home-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="climate-service",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Climate Service Running...")

for msg in consumer:
    event = msg.value

    if event["type"] == "temperature":
        temp = event["value"]

        if temp > 30:
            print("❄ AC ON:", temp)
        elif temp < 18:
            print("🔥 HEATER ON:", temp)
        else:
            print("✔ Comfortable:", temp)
