from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.forms.users import UserModify

bp = Blueprint("admin", __name__)


@bp.route("/")
@login_required
def index():
    if current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    form = UserModify()

    return render_template("admin.html", title="Administration", form=form)
