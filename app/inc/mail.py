from typing import List
from flask_mail import Mail, Message
from app.config import ConfigEmail


# Global object for mail app purpose
obj_mail = None


def init_mail(app):
    global obj_mail
    app.config["MAIL_SERVER"] = ConfigEmail.MAIL_SERVER
    app.config["MAIL_PORT"] = ConfigEmail.MAIL_PORT
    app.config["MAIL_USERNAME"] = (
        ConfigEmail.MAIL_SENDER
    )  # Use your actual Gmail address
    app.config["MAIL_PASSWORD"] = (
        ConfigEmail.MAIL_PASSWORD
    )  # Use your generated App Password
    app.config["MAIL_USE_TLS"] = ConfigEmail.MAIL_USE_TLS
    app.config["MAIL_USE_SSL"] = ConfigEmail.MAIL_USE_SSL
    # print("###### app.config: ", app.config)
    obj_mail = Mail(app)
    return obj_mail

    """
    mail = Mail(app)
    msg = Message(
        subject='Hello from little garden from !', 
        sender='your_email@gmail.com',  # Ensure this matches MAIL_USERNAME
        recipients=['recipient@example.com']  # Replace with actual recipient's email
    )
    msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
    mail.send(msg)
    return "Message sent!"
    """


def send_mail_html(send_to: List[str], subject: str, message: str):
    return send_mail(
        send_to=send_to, subject=subject, message=message, is_message_html=True
    )


def send_mail(
    send_to: List[str], subject: str, message: str, is_message_html: bool = False
):
    msg = Message(
        sender=ConfigEmail.MAIL_SENDER,
        recipients=send_to,
        subject=subject,
    )
    if is_message_html:
        msg.html = message
    else:
        msg.body = message

    result = True
    error = None
    if obj_mail:
        try:
            obj_mail.send(msg)
        except Exception as err:
            result = False
            error = f"ERROR: app/inc/mail.py - {err=}"
            print(f"{error}, {type(err)=}")
    else:
        result = False
        error = "ERROR: app/inc/mail.py - obj_mail not initialized, use init_mail."

    return {
        "result": result,
        "error": error,
    }
