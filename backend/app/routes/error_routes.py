from fastapi import APIRouter
from app.services.logger_service import log_error
from app.database import supabase
from app.models.error_model import ErrorLog
from collections import Counter

router = APIRouter()

@router.post("/log-error")
def manual_log_error(error: ErrorLog):
    # Convert Pydantic model to dict
    error_dict = error.model_dump()
    log_error(error_dict)
    return {"message": "Error logged successfully"}

@router.get("/errors")
def get_errors():
    response = supabase.table("errors").select("*").order("timestamp", desc=True).execute()
    return response.data

@router.get("/errors/critical")
def get_critical_errors():
    response = supabase.table("errors").select("*").eq("is_critical", True).order("timestamp", desc=True).execute()
    return response.data

@router.get("/errors/stats")
def get_error_stats():
    # Fetch just status codes to minimize data transfer
    response = supabase.table("errors").select("status_code").execute()
    
    # Aggregate in Python
    status_counts = Counter(item['status_code'] for item in response.data)
    
    # Format to match previous API response: [{"_id": code, "count": num}]
    stats = [{"_id": code, "count": count} for code, count in status_counts.items()]
    return stats
