# 🎓 Error Sentinel - Interview Q&A Guide

## Q1: Tell me about your project?
**Answer:**
"Sir/Ma'am, I built an **Error Tracking & Alerting System**.
In real-world software, when a crash happens (like a Payment Failure), developers often don't know until a user complains.
My system solves this by acting as a **Centralized Log Server**. It connects to applications, detects errors in real-time, displays them on a dashboard, and sends **Instant Email Alerts** for critical issues."

---

## Q2: How do other projects actually use this? Where is it used? (Use Cases)
**Answer:**
"This is designed as a **Microservice** or a **Centralized Logger**."

### **Scenario:**
Imagine a company has 3 different applications running:
1.  **User App** (React Native) - For customers.
2.  **Delivery App** (Android) - For delivery boys.
3.  **Admin Portal** (Web) - For management.

If the *Delivery App* crashes, I don't want to go and check the mobile phone logs.
Instead, all 3 apps are connected to my **Error Sentinel**.

### **How they integrate:**
In every application, inside the `try-catch` block (where we handle errors), the developer simply adds one line of code:
`send_alert(error_message)`

This sends the error data to my central API (`/log-error`).
So, no matter where the error comes from (Mobile, Web, or Backend), it lands in **ONE Dashboard**.

**Benefits:**
1.  **Central Visibility:** Monitor 10 different projects in one place.
2.  **Proactive:** We fix errors before users even report them.
3.  **Time Saving:** No need to dig through server text files.

---

## Q3: What is the challenging part of this project?
**Answer:**
"The main challenge was handling **Real-time Concurrency**. If 100 errors come at once, the system shouldn't crash.
I solved this by using **FastAPI's asynchronous (async/await)** capabilities, which allows it to handle many requests without blocking."

## Q4: How is this better than simply writing logs to a file?
**Answer:**
"Text logs are **passive**. You have to go and read them.
My system is **active**. It notifies YOU when something is wrong (via Email). It's the difference between a CCTV Camera (Recording) and a Burglar Alarm (Ringing)."
