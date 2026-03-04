from datetime import datetime, timezone
import os
import requests
from fastapi import FastAPI

app = FastAPI()

LOGGER_URL = os.getenv("LOGGER_URL", "http://logger-api:8000/log")


@app.get("/time")
def get_time():
    now = datetime.now(timezone.utc).isoformat()
    try:
        requests.post(LOGGER_URL, json={"iso": now}, timeout=0.5)
    except Exception:
        pass
    return {"iso": now}
