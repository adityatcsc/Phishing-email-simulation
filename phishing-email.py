import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# Email configuration
SMTP_SERVER = 'smtp.google.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@example.com'
SENDER_PASSWORD = 'your_password'

# Phishing email templates
email_templates = [
    {
        'subject': 'URGENT: Your account needs attention',
        'body': 'Dear customer, your account is in danger. Click this link to verify your information: [your phishing-link]'
    },
    {
        'subject': 'Important security update',
        'body': 'We have detected unauthorized activity on your account. Click here to secure your account: [your phishing-link]'
    }
]

def send_phishing_email(target_email):
    # Select a random email template
    template = random.choice(email_templates)

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = target_email
    msg['Subject'] = template['subject']

    # Add message body
    msg.attach(MIMEText(template['body'], 'plain'))

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    target_email = input("Enter target email address: ")
    send_phishing_email(target_email)
    print("Phishing email sent successfully!")
