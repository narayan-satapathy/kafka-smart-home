from kafka import KafkaProducer
import json
import random
import time
from common.event_schema import create_event

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    event = create_event(
        device="temperature_sensor",
        event_type="temperature",
        value=random.randint(15, 40)
    )

    producer.send("smart-home-events", event)
    print("sent:", event)

    time.sleep(2)
