from fastapi import FastAPI

app = FastAPI()


@app.post("/log")
def log_time(payload: dict):
    # 간단히 출력만 하는 로거
    print("[logger-api] payload:", payload)
    return {"status": "ok"}
