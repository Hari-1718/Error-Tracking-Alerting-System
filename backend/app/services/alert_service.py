from app.utils.email_utils import send_email

def check_and_alert(error_data: dict):
    # Trigger alert only for critical errors
    if error_data.get("is_critical"):
        subject = f"CRITICAL ALERT: {error_data.get('api_name', 'Unknown API')} Failed"
        body = f"""
        Critical Error Detected!
        
        API: {error_data.get('api_name')}
        Status: {error_data.get('status_code')}
        Message: {error_data.get('error_message')}
        Time: {error_data.get('timestamp')}
        """
        send_email(subject, body)
