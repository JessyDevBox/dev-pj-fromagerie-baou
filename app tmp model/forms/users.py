# app/forms/users.py
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from app.routes.auth import UserRights
from app.models import User


class UserModify(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=64)]
    )
    rights = SelectField(
        "Rights", choices=[(UserRights.user, "User"), (UserRights.admin, "Admin")]
    )
    submit = SubmitField("Modify")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already used.")
