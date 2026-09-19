from fastapi import FastAPI
from pydantic import BaseModel
from agent import db_agent

app = FastAPI(title="LogSense Real")

class LogRequest(BaseModel):
    log: str

@app.get("/")
def home():
    return {"message": "LogSense Real - Built Today - Running"}

@app.post("/analyze")
def analyze(req: LogRequest):
    diagnosis = db_agent(req.log)
    return diagnosis

@app.post("/dedup-demo")
def dedup_demo():
    # Your today logic as an API
    from main import test_logs
    unique_logs = list(set(test_logs))
    return {
        "total_logs": len(test_logs),
        "unique_logs": len(unique_logs),
        "reduction": f"{100 - (len(unique_logs)/len(test_logs)*100):.0f}%",
        "logs": unique_logs
    }