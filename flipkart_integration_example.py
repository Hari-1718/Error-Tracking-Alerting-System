# 🛒 FLIPKART CODEBASE (Example)

import requests
from error_sentinel_client import send_alert  # <--- Step 1: Import mana code

def process_payment(user_id, amount):
    print(f"Processing payment of ₹{amount} for User {user_id}...")
    
    try:
        # --- FLIPKART REAL LOGIC ---
        # Bank server ki connect avuthundi...
        bank_response = requests.post("https://bank-server.com/pay", timeout=2)
        
        # Okavela Bank Server Down ayithe?? 💥
        bank_response.raise_for_status()
        
        print("Payment Successful! ✅")
        return True

    except Exception as e:
        # --- IKKADA!! (WHERE TO INTEGRATE) ---
        print("Payment Failed! ❌")
        
        # Mana Error Sentinel ni pilustam:
        send_alert(
            error_message=f"Payment Failed for User {user_id}: {str(e)}", 
            api_name="Flipkart Payment Gateway",
            is_critical=True
        )
        
        # User ki just simple message chupistam
        return "Sorry, Payment Failed. Try again."
