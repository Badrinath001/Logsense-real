# Real Pydantic model from your resume - No API needed for Day 1
from pydantic import BaseModel
from typing import Literal

class Diagnosis(BaseModel):
    error_type: Literal["DB", "Memory", "Network", "Security"]
    service: str
    confidence: float
    fix_action: str

def db_agent(log: str) -> Diagnosis:
    """This is your REAL agent logic - same as LangGraph will use"""
    log_lower = log.lower()
    if "db" in log_lower or "connection" in log_lower:
        return Diagnosis(
            error_type="DB", 
            service="hostel-service", 
            confidence=0.95, 
            fix_action="Restart PostgreSQL, check DB_HOST, increase connection pool"
        )
    elif "memory" in log_lower or "leak" in log_lower:
        return Diagnosis(
            error_type="Memory", 
            service="mess-service", 
            confidence=0.92, 
            fix_action="Clear Redis cache, restart service, check for memory leak"
        )
    else:
        return Diagnosis(
            error_type="Network", 
            service="library-service", 
            confidence=0.85, 
            fix_action="Check timeout config, retry with exponential backoff"
        )

if __name__ == "__main__":
    test = "[ERROR] DB connection failed - hostel-service"
    print(db_agent(test))