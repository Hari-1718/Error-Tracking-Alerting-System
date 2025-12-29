import requests
from datetime import datetime
import threading

# CONFIGURATION
# Miku vere user ki iche code idhe.
# Vallu just ee URL ni change cheskunte chalu (mee IP address or hosted URL ivvali).
SENTINEL_URL = "http://localhost:8000/log-error"

def send_alert(error_message, api_name="Unknown Function", status_code=500, is_critical=True):
    """
    Sends an error alert to the Error Sentinel system.
    This runs in the background so it doesn't slow down the main app.
    """
    def _send():
        try:
            payload = {
                "api_name": api_name,
                "status_code": status_code,
                "error_message": str(error_message),
                "is_critical": is_critical,
                "timestamp": datetime.now().isoformat()
            }
            requests.post(SENTINEL_URL, json=payload, timeout=5)
            print("✅ Error Report Sent to Sentinel!")
        except Exception as e:
            print(f"⚠️ Failed to send error report: {e}")

    # Run in background to avoid blocking
    threading.Thread(target=_send).start()

# Example Usage (Test)
if __name__ == "__main__":
    send_alert("Database Connection Timeout", api_name="/user/login", is_critical=True)
