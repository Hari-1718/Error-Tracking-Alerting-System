# Error Sentinel 🛡️

A production-ready Fullstack Error Tracking System designed to automatically detect application failures, log them securely, and alert developers instantly.

---

## 💡 The Core Idea

In real-world applications, errors are inevitable. However, the problem is often:
- Developers realize the error **too late**.
- Users have to **complain** before a fix is initiated.

**Error Sentinel** solves this by:
1.  **Detecting** errors automatically.
2.  **Logging** them instantly to a cloud database (Supabase).
3.  **Alerting** the developer via Email for critical failures (5xx errors).

### Real-Life Example
Imagine a user on a shopping app clicks "Place Order" and gets a **500 Internal Server Error**.
- **Normally**: The user is frustrated, and the developer has no clue.
- **With Error Sentinel**: The system captures the crash, logs the stack trace, and sends an email: *"Checkout API failed at 10:32 AM - Database Connection Refused"*. The developer fixes it before more users are affected.

---

## 🏗 Architecture Flow

1.  **API Error Occurs**: 
    - `4xx` (User Mistake like "Invalid Login")
    - `5xx` (Server Crash like "DB Down") - **Critical**
2.  **Error Logging**:
    - Captures `API Name`, `Status Code`, `Error Message`, `Time`.
    - Stores efficiently in **Supabase (PostgreSQL)**.
3.  **Critical Detection**:
    - Middleware analyzes the status code.
    - If `5xx`, it is flagged as **Critical**.
4.  **Instant Alert**:
    - The backend uses SMTP to send an immediate email to the developer.
5.  **Dashboard & Analysis**:
    - A React + Vite Dashboard displays trends, error counts, and recent logs.

---

## 🛠 Tech Stack

- **Backend**: Python (FastAPI), Supabase (DB), Pydantic (Validation), SMTP (Email).
- **Frontend**: React, Vite, TailwindCSS, Recharts, TanStack Query.
- **Tools**: VS Code, Git.

---

## 🚀 How to Run

### Prerequisite
Make sure you have `python` and `node` installed.

### 1. Start Backend
```powershell
cd backend
.\run.bat
# Runs on http://localhost:8000
```

### 2. Start Frontend
```powershell
cd frontend
.\run.bat
# Runs on http://localhost:5173
```

---

## 🧠 Interview Q&A

**Q: Why is this project important?**
> "It minimizes downtime and improves user experience by shifting from 'reactive' debugging (waiting for complaints) to 'proactive' fixing (instant alerts)."

**Q: What improvements did you make?**
- Added a **Real-time Dashboard** for visual monitoring.
- Implemented **Email Alerts** for critical issues.
- Migrated to **Supabase** for scalable cloud storage.

---

## 📂 Project Structure
- `backend/app`: FastAPI server logic.
- `frontend/src`: React dashboard UI.

