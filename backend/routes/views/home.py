from flask import Blueprint, redirect, url_for, render_template

from backend.routes import get_blueprint_name, VIEWS_BASE_NAME

HOME_BLUEPRINT_NAME = "home"
home_blueprint = Blueprint(
    get_blueprint_name(VIEWS_BASE_NAME, HOME_BLUEPRINT_NAME), __name__
)


@home_blueprint.route("/")
def index():
    return redirect(url_for(f"{HOME_BLUEPRINT_NAME}.home"))


@home_blueprint.route("/home")
def home():
    return render_template("home.html")
