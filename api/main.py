import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://app:app@db:5432/appdb")


@app.get("/rows")
def list_rows():
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, created_at FROM items ORDER BY id")
            rows = cur.fetchall()
    return {
        "rows": [
            {"id": r[0], "name": r[1], "created_at": r[2].isoformat()} for r in rows
        ]
    }
