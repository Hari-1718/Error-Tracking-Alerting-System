import smtplib
from email.mime.text import MIMEText
from app.config import settings

def send_email(subject: str, body: str):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = settings.SMTP_USERNAME
        msg["To"] = settings.ALERT_RECIPIENT

        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.sendmail(settings.SMTP_USERNAME, settings.ALERT_RECIPIENT, msg.as_string())
        return True
    except Exception as e:
        # Log failure silently or print to console (graceful failure)
        print(f"Failed to send email: {e}")
        return False
