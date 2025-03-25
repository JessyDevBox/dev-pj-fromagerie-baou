# app/forms/auth.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me recorded")
    submit = SubmitField("Connecte")


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=64)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(
        "Repeat password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Suscribe")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already used.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Mail already used.")
