# app/routes/sandbox.py
from flask import Blueprint, render_template, flash
from app.inc.mail import send_mail
from flask_login import current_user


bp = Blueprint("sandbox", __name__)


@bp.route("/")
def index():
    ctx = {
        "title": "HOME of Sandbox",
        "description": "Test 101",
    }
    return render_template(
        "sandbox.html",
        ctx=ctx,
    )


@bp.route("/test")
def test():
    ctx = {
        "title": "TEST SUB-PAGE of Sandbox",
        "description": "Test 201",
    }
    return render_template(
        "sandbox.html",
        ctx=ctx,
    )


@bp.route("/mail")
def mail():
    description = "Try send mail..."

    mail_result = send_mail(
        send_to=["jessythegamer@gmail.com"],
        subject="TEST Email from TinyGarden",
        message="TEST - My awsome message from TinyGarden.",
    )

    if mail_result["result"]:
        description += " Mail Sent with success!"
        flash("Mail successfully SENT!", "success")
    else:
        description += f" ** {mail_result['error']}"
        flash(f"ERROR when sending mail. *** {mail_result['error']} ***", "danger")

    ctx = {
        "title": "TEST - MAIL",
        "description": description,
    }
    return render_template(
        "sandbox.html",
        ctx=ctx,
    )


@bp.route("/mail_current_user")
def mail_current_user():
    mail = None
    if current_user.is_authenticated:
        if current_user.email:
            mail = current_user.email

    if mail:
        mail_result = send_mail(
            send_to=[mail],
            subject="TEST Email from TinyGarden",
            message=f"""
            <html>
                <body>
                    <h1>TEST - Tiny Garden</h1>
                    <h3>My awsome message from TinyGarden, to current user: {mail}</h3>
                </body>
            </html>
            """,
            is_message_html=True,
        )

        if mail_result["result"]:
            flash("Mail successfully SENT!", "success")
        else:
            flash(f"ERROR when sending mail. *** {mail_result['error']} ***", "danger")
    else:
        flash("Current user not found! Please login", "danger")

    desc = f"Try sending mail to current user: {mail}"
    ctx = {
        "title": "TEST - MAIL - Send to current user",
        "description": desc,
    }
    return render_template(
        "sandbox.html",
        ctx=ctx,
    )
