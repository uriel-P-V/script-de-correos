import smtplib
from mail_content import content
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from contacts import contacts

failed_list = []

email = "hello@ejemplo.org"
password = "G4adalajara 2020"

with smtplib.SMTP_SSL('mail.ejemplo.org', 465) as smtp:
    smtp.login(email, password)

    for name, mail in contacts.items():
        try:
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = mail
            msg['Subject'] = "Hello"

            # Create the message body
            body = content.format(name, mail, name, name, mail, name)
            msg.attach(MIMEText(body, 'plain', 'utf-8'))  # Attach body with UTF-8 encoding

            # Send the email
            smtp.sendmail(email, mail, msg.as_string())

        except Exception as e:
            failed_list.append((name, mail))
            print(f"Failed to send email to {name} ({mail}): {str(e)}")

if failed_list:
    print("Failed to send emails to the following recipients:")
    for name, mail in failed_list:
        print(f"{name} ({mail})")
else:
    print("All emails sent successfully.")
