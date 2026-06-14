from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

i = 1

while True:
    event = {
        "event_id": i,
        "type": "demo",
        "message": "hello kafka stream"
    }

    producer.send("smart-home-events", value=event)
    print("sent:", event)

    i += 1
    time.sleep(2)
