import requests
import json
import time
from datetime import datetime

# System URL (The Police Station)
ERROR_SENTINEL_URL = "http://localhost:8000/log-error"

def simulate_shopping_crash():
    print("🛒 Starting Fake Shopping App...")
    time.sleep(1)
    
    print("💳 User is clicking 'Pay Now'...")
    time.sleep(1)
    
    print("❌ CRASH! Payment Gateway Failed!")
    
    # Error Data to send
    error_payload = {
        "api_name": "/api/checkout/payment",
        "status_code": 503,
        "error_message": "Payment Gateway Timeout - Third Party Service Down",
        "is_critical": True,
        "timestamp": datetime.now().isoformat()
    }
    
    # Sending to Error Sentinel
    try:
        error_payload["timestamp"] = datetime.now().isoformat()
        
        print(f"📡 Sending Error Report to {ERROR_SENTINEL_URL}...")
        response = requests.post(ERROR_SENTINEL_URL, json=error_payload)
        
        if response.status_code == 200:
            print("\n✅ Success! Error Sentinel received the alert.")
            print("Check your Dashboard now!")
        else:
            print(f"⚠️ Failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Connection Error: Is the backend running? {e}")

if __name__ == "__main__":
    simulate_shopping_crash()
