from flask import Blueprint, session, request, jsonify

from backend.api import getLinks, cadastroLink
from backend.routes import get_blueprint_name, API_BASE_NAME
from backend.utils.decorators import is_logged_in
from backend.utils.responses import success_response, error_response

api_links_blueprint = Blueprint(get_blueprint_name(API_BASE_NAME, "links"), __name__)


@api_links_blueprint.route("/api/links/<int:id_disciplina>")
@is_logged_in
def apiLinks(id_disciplina):
    data = getLinks(id_disciplina)
    return jsonify(data)


@api_links_blueprint.route("/api/cadastro/link", methods=["POST"])
@is_logged_in
def apiCadastroLink():
    r = request.get_json()

    id_disciplina = r.get("id_disciplina")
    titulo = r.get("titulo")
    link = r.get("link")
    id_user = session.get("id")

    success, message = cadastroLink(id_user, id_disciplina, titulo, link)
    if success:
        return success_response()
    else:
        return error_response(message)
