from flask import Blueprint, jsonify, request, session

from backend.api import (
    getDisciplinas,
    getDisciplina,
    getTopDisciplinas,
    cadastroDisciplina,
    cadastroAvaliacaoDisciplina,
)
from backend.routes import get_blueprint_name, API_BASE_NAME
from backend.utils.decorators import is_logged_in
from backend.utils.responses import success_response, error_response

api_disciplinas_blueprint = Blueprint(
    get_blueprint_name(API_BASE_NAME, "disciplinas"), __name__
)


@api_disciplinas_blueprint.route("/api/disciplinas")
def apiDisciplinas():
    r = getDisciplinas()
    return jsonify(r)


@api_disciplinas_blueprint.route("/api/disciplina/<int:id_disciplina>")
@is_logged_in
def apiDisciplina(id_disciplina):
    r = getDisciplina(id_disciplina)
    return jsonify(r)


@api_disciplinas_blueprint.route("/api/disciplinas/top/<int:n>/<string:categoria>")
def apiTopDisciplinas(n, categoria):
    data = getTopDisciplinas(n, categoria)
    return jsonify(data)


@api_disciplinas_blueprint.route("/api/cadastro/disciplina", methods=["POST"])
@is_logged_in
def apiCadastroDisciplina():
    r = request.get_json()

    nome = r.get("nome")
    penoso_mamao = r.get("penoso_mamao")
    id_user = session.get("id")

    success, message = cadastroDisciplina(nome, penoso_mamao, id_user)

    if success:
        return success_response()
    else:
        return error_response(message)


@api_disciplinas_blueprint.route("/api/cadastro/avaliacao_disciplina", methods=["POST"])
@is_logged_in
def apiCadastroAvaliacaoDisciplina():
    r = request.get_json()

    id_disciplina = r.get("id_disciplina")
    penoso_mamao = r.get("penoso_mamao")
    id_user = session.get("id")

    success, message = cadastroAvaliacaoDisciplina(penoso_mamao, id_disciplina, id_user)

    if success:
        return success_response()
    else:
        return error_response(message)
