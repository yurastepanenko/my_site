from flask_mail import Mail,Message
import os

mail = Mail()


def send_mail(title,
              body,
              recipients=[]):
    message = Message(title,
                      sender=os.environ["MAIL_USERNAME"],
                      body=body,
                      recipients=recipients)
    mail.send(message)
