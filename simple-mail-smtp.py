import smtplib

s = smtplib.SMTP('smtp.example.com', 587)

# security
s.starttls()

# Authentication
s.login("your_email_id@example.com", "your_email_id_password")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("your_email_id@example.com", "sender_email_id@example.com", message)
s.quit()
