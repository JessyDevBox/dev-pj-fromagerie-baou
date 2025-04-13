from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from app.forms import LoginForm, RegistrationForm

# Création des blueprints
main_bp = Blueprint("main", __name__)
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# Routes principales
@main_bp.route("/")
@main_bp.route("/home")
def home():
    return render_template("home.html", title="Accueil")


# Routes d'authentification
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Nom d'utilisateur ou mot de passe incorrect", "danger")
            return redirect(url_for("auth.login"))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        return redirect(next_page if next_page else url_for("main.home"))

    return render_template("login.html", title="Connexion", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(
            "Votre compte a été créé avec succès! Vous pouvez maintenant vous connecter.",
            "success",
        )
        return redirect(url_for("auth.login"))

    return render_template("register.html", title="Inscription", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
