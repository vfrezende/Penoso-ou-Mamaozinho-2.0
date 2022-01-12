from flask import Blueprint, redirect, url_for, render_template, session

from backend.routes import get_blueprint_name, VIEWS_BASE_NAME
from backend.utils.decorators import is_logged_in

usuarios_blueprint = Blueprint(
    get_blueprint_name(VIEWS_BASE_NAME, "usuarios"), __name__
)


@usuarios_blueprint.route("/register")
def cadastro():
    return render_template("register.html")


@usuarios_blueprint.route("/profile")
def profile():
    return render_template("profile.html")


@usuarios_blueprint.route("/login")
def login():
    return render_template("login.html")


@usuarios_blueprint.route("/logout")
@is_logged_in
def logout():
    session.clear()
    return redirect(url_for("home"))
