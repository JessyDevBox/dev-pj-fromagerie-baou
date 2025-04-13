from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
    remember_me = BooleanField("Se souvenir de moi")
    submit = SubmitField("Se connecter")


class RegistrationForm(FlaskForm):
    username = StringField(
        "Nom d'utilisateur", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Mot de passe", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirmer le mot de passe", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("S'inscrire")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "Cet email est déjà utilisé. Veuillez en choisir un autre."
            )
