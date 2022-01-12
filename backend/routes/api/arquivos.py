from flask import Blueprint, jsonify, request, send_file, session
from backend.api import cadastro_arquivo, get_arquivo, get_arquivos_informacoes
from backend.routes import get_blueprint_name
from backend.routes import API_BASE_NAME
from backend.utils.decorators import is_logged_in
from backend.utils.responses import error_response, success_response

api_arquivos_blueprint = Blueprint(
    get_blueprint_name(API_BASE_NAME, "arquivos"), __name__
)


@api_arquivos_blueprint.route(
    "/api/arquivos/<int:id_disciplina>", methods=["GET", "POST"]
)
@is_logged_in
def api_arquivos(id_disciplina):
    data = get_arquivos_informacoes(id_disciplina)
    return jsonify(data)


@api_arquivos_blueprint.route("/api/arquivo/<int:id_arquivo>", methods=["GET", "POST"])
@is_logged_in
def api_arquivo(id_arquivo):
    arquivo = get_arquivo(id_arquivo)
    return send_file(
        arquivo["dados"],
        mimetype=arquivo["mimetype"],
        attachment_filename=arquivo["nome"],
        as_attachment=True,
    )


@api_arquivos_blueprint.route("/api/cadastro/arquivo", methods=["POST"])
@is_logged_in
def api_cadastro_arquivo():
    r = request.get_json()

    id_disciplina = r.get("id_disciplina")
    nome = r.get("nome")
    mimetype = r.get("mimetype")
    descricao = r.get("descricao")
    dados = r.get("dados")
    id_user = session.get("id", 5)

    success, message = cadastro_arquivo(
        id_user, id_disciplina, nome, mimetype, descricao, dados
    )
    if success:
        return success_response()
    else:
        return error_response(message)
