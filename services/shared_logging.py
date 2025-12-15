import json, time, sys

def log(event, **data):
    payload = {
        "ts": time.time(),
        "event": event,
        "data": data
    }
    print(json.dumps(payload), flush=True)
