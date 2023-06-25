import smtplib
import imghdr
import os
from email.message import EmailMessage


def send_email(image):
    print("Send_Email Function started")
    email_msg = EmailMessage()
    email_msg["Subject"] = "New customer entered the shop."
    email_msg.set_content("Hello, there is a new customer.")
    with open(image, "rb") as file:
        content = file.read()
    email_msg.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    # Setting up the email
    host = "smtp.gmail.com"
    port = 587

    username = "bellasara13@gmail.com"
    password = os.getenv("PASSWORD")

    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, username, email_msg.as_string())

    print("Send_Email Function ended")

if __name__ == "__main__":
    send_email(image="images/1.png")
