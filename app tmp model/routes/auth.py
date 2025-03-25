# app/routes/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from app import db
from app.forms.auth import LoginForm, RegistrationForm
from app.inc.mail import send_mail_html

from app.models import User

bp = Blueprint("auth", __name__)


class UserRights:
    default = 1
    user = 1
    admin = 9


@bp.route("/")
def index():
    return render_template(
        "sandbox.html", ctx={"title": "Route /auth/", "from": "!!Auth!!"}
    )


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("garden.list"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("auth.login"))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlparse(next_page).netloc != "":
            next_page = url_for("garden.list")
        return redirect(next_page)

    return render_template("auth/login.html", title="Connexion", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("garden.list"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user = User(
            username=form.username.data,
            email=form.email.data,
            rights=UserRights.default,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Success you suscribed!", "success")

        mail_result = send_mail_html(
            send_to=[user_email],
            subject="Tiny Garden - Subscription Success",
            message=f"""
            <html>
                <body>
                    <h1>Mini Jardin</h1>
                    <h3>Bienvenue {form.username.data} sur le site de mini jardin.</h3>
                    <h3>Passez une bonne journée dans votre jardin</h3>
                </body>
            </html>
            """,
        )
        if not mail_result["result"]:
            flash(f"ERROR when sending mail. *** {mail_result['error']} ***", "danger")

        return redirect(url_for("route.index"))

    return render_template("auth/register.html", title="Inscription", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("route.index"))


# User modify rights
@bp.route("/user/<int:user_id>/rights", methods=["POST"])
@login_required
def user_rights_update(user_id):
    route_to_admin = "route.index"  # <-- TOUPDATE
    # Valid if current_user has admin rights
    if not current_user.rights == UserRights.admin:
        flash("You shoud be an admin in order to change user rights!", "error")
        return redirect(url_for(route_to_admin))

    # Getting user to modify
    user = User.query.get_or_404(user_id)

    # Getting rights form form
    new_rights = request.form.get("rights")

    # Valid if rights match
    if new_rights not in [UserRights.default, UserRights.user, UserRights.admin]:
        flash(
            f"Rights: [{new_rights}] for user: {user.username} doesn't exists, no change made!",
            "error",
        )
        return redirect(url_for(route_to_admin))

    # Update right in DB
    user.rights = new_rights
    db.session.commit()

    flash(
        f"Rights: [{new_rights}] for user: {user.username} successfully changed!",
        "success",
    )
    return redirect(url_for(route_to_admin))
