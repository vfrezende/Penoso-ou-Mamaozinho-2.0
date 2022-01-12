from flask import Blueprint, render_template

from backend.routes import get_blueprint_name, VIEWS_BASE_NAME
from backend.utils.decorators import is_logged_in

disciplinas_blueprint = Blueprint(
    get_blueprint_name(VIEWS_BASE_NAME, "disciplinas"), __name__
)


@disciplinas_blueprint.route("/disciplina/<int:id_disciplina>")
@is_logged_in
def disciplina(id_disciplina):
    return render_template("disciplina.html")


@disciplinas_blueprint.route("/adicionar_disciplina")
@is_logged_in
def adicionar_disciplina():
    return render_template("adicionar_disciplina.html")
