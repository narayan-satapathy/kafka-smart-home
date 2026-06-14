from datetime import datetime
import uuid

def create_event(device, event_type, value):
    return {
        "event_id": str(uuid.uuid4()),
        "device": device,
        "type": event_type,
        "value": value,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
