from email.message import EmailMessage
import ssl  # to encrypt the email
import smtplib  # to send our email


email_sender = 'your_email@gmail.com'
email_password = 'custom password for apps'

email_receiver = 'receiver@hotmail.com'

subject = 'subject'
body = """
message content

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

# Define the body of the email
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)  # Logging in your account
    # em.as_string() receive all 'em' and transform as a string
    smtp.sendmail(email_sender, email_receiver, em.as_string())
