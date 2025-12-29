from app.database import supabase
from app.services.alert_service import check_and_alert
from datetime import datetime

def log_error(error_data: dict):
    # Ensure timestamp is ISO string if it's a datetime object
    if isinstance(error_data.get("timestamp"), datetime):
        error_data["timestamp"] = error_data["timestamp"].isoformat()

    # Insert into Supabase 'errors' table
    supabase.table("errors").insert(error_data).execute()
    
    # Check for alerts
    check_and_alert(error_data)
