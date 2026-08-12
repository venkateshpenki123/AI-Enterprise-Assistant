from fastapi import FastAPI
from pydantic import BaseModel

from sql_agent import get_tables, execute_sql


app = FastAPI(
    title="AI Enterprise Assistant API",
    description="REST API for the Enterprise Assistant",
    version="1.0.0"
)


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():

    return {
        "status": "running",
        "message": "AI Enterprise Assistant API is working"
    }


# ==========================================
# GET DATABASE TABLES
# ==========================================

@app.get("/tables")
def tables():

    return {
        "tables": get_tables()
    }


# ==========================================
# SQL REQUEST MODEL
# ==========================================

class SQLRequest(BaseModel):

    query: str


# ==========================================
# EXECUTE SQL
# ==========================================

@app.post("/sql")
def run_sql(request: SQLRequest):

    try:

        result = execute_sql(
            request.query
        )

        return {
            "success": True,
            "data": result.to_dict(
                orient="records"
            )
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }