from flask import Blueprint, session, request, jsonify

from backend.api import (
    getComentarios,
    cadastroAvaliacaoComentario,
    deletarComentario,
    cadastroComentario,
    denunciarComentario,
)
from backend.routes import get_blueprint_name, API_BASE_NAME
from backend.utils.decorators import is_logged_in
from backend.utils.responses import success_response, error_response

api_comentarios_blueprint = Blueprint(
    get_blueprint_name(API_BASE_NAME, "comentarios"), __name__
)


@api_comentarios_blueprint.route("/api/comentarios/<int:id_disciplina>")
@is_logged_in
def apiComentarios(id_disciplina):
    data = getComentarios(id_disciplina)
    return jsonify(data)


@api_comentarios_blueprint.route("/api/cadastro/avaliacao_comentario", methods=["POST"])
@is_logged_in
def apiCadastroAvaliacaoComentario():
    r = request.get_json()

    id_comentario = r.get("id_comentario")
    like_dislike = r.get("like_dislike")
    id_user = session.get("id")

    success, message = cadastroAvaliacaoComentario(id_comentario, like_dislike, id_user)

    if success:
        return success_response()
    else:
        return error_response(message)


@api_comentarios_blueprint.route("/api/cadastro/deletar_comentario", methods=["POST"])
@is_logged_in
def apiDeletarComentario():
    r = request.get_json()

    id_comentario = r.get("id_comentario")
    username = session.get("username")

    success, message = deletarComentario(id_comentario, username)
    if success:
        return success_response()
    else:
        return error_response(message)


@api_comentarios_blueprint.route("/api/cadastro/comentario", methods=["POST"])
@is_logged_in
def apiCadastroComentario():
    r = request.get_json()

    id_disciplina = r.get("id_disciplina")
    comentario = r.get("comentario")
    id_user = session.get("id")

    success, message = cadastroComentario(id_user, id_disciplina, comentario)
    if success:
        return success_response()
    else:
        return error_response(message)


@api_comentarios_blueprint.route("/api/cadastro/denunciar_comentario", methods=["POST"])
@is_logged_in
def apiDenunciarComentario():
    r = request.get_json()

    id_comentario = r.get("id_comentario")
    id_user = session.get("id")

    success, message = denunciarComentario(id_comentario, id_user)
    if success:
        return success_response()
    else:
        return error_response(message)
