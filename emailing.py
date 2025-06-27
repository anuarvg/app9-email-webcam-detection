import smtplib
import ssl
from email.message import EmailMessage
import imghdr

SENDER = "anuar.vasquez@tcpip.tech"
PASSWORD = "odirevfxjaidjsaf"

host = "smtp.gmail.com"
port = 465
def send_email(image_path):
    context = ssl.create_default_context()
    receiver = "anuarvg@gmail.com"
    email_message = EmailMessage()
    email_message["Subject"] = "Llego nuevo usuario"
    email_message.set_content("Hey, nosotros vimos un nuevo cliente")

    with open(image_path, "rb") as image:
        content = image.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER,receiver, email_message.as_string())

    print("Email was sent!")

# if __name__ == "__main__":
#     send_email(image_path="images/10.png")