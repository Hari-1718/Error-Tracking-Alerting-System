# 🔌 How to Connect Your Project to Error Sentinel

To connect any application (Shopping App, Food App, etc.) to Error Sentinel, you just need to send a web request whenever an error occurs.

Here are the code snippets you can copy-paste into your other projects.

---

## 🟢 1. Node.js (Express / MERN Stack)

If you have a Node.js backend, add this function to your error handler:

```javascript
const axios = require('axios');

// Function to send error to Error Sentinel
async function reportErrorToSentinel(error, req) {
  try {
    await axios.post('http://localhost:8000/log-error', {
      api_name: req.path,           // e.g., "/login"
      status_code: 500,             // e.g., 500
      error_message: error.message, // e.g., "Database connection failed"
      is_critical: true,            // Mark as critical for email alert
      timestamp: new Date().toISOString()
    });
    console.log("✅ Error reported to Sentinel");
  } catch (err) {
    console.error("❌ Failed to report error:", err.message);
  }
}

// Global Error Handler Middleware
app.use((err, req, res, next) => {
  // 1. Send alert
  reportErrorToSentinel(err, req);
  
  // 2. Send response to user
  res.status(500).json({ error: "Internal Server Error" });
});
```

---

## 🐍 2. Python (FastAPI / Flask)

If you have a Python backend, use this:

```python
import requests
from datetime import datetime

def report_error_to_sentinel(api_path, error_msg, status=500):
    try:
        payload = {
            "api_name": api_path,
            "status_code": status,
            "error_message": str(error_msg),
            "is_critical": True if status >= 500 else False,
            "timestamp": datetime.now().isoformat()
        }
        requests.post('http://localhost:8000/log-error', json=payload)
    except Exception as e:
        print(f"Failed to report error: {e}")

# Usage inside an API
try:
    # Your code that might fail
    result = 1 / 0 
except Exception as e:
    report_error_to_sentinel("/calculate", str(e), 500)
```

---

## 🌐 3. React (Frontend)

You can even report errors from the browser!

```javascript
const reportError = async (message) => {
  await fetch("http://localhost:8000/log-error", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      api_name: window.location.pathname,
      status_code: 400,
      error_message: message,
      is_critical: false,
      timestamp: new Date().toISOString()
    })
  });
};
```
