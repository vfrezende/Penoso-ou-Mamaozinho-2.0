from flask import Blueprint, session, request

from backend.api import checkUsuario, cadastroUsuario, getUsuario, updateUsuario
from backend.routes import get_blueprint_name, API_BASE_NAME
from backend.utils.decorators import is_logged_in
from backend.utils.responses import success_response, error_response
from backend.utils.utils import update_session

api_usuarios_blueprint = Blueprint(get_blueprint_name(API_BASE_NAME, "user"), __name__)


@api_usuarios_blueprint.route("/api/usuario", methods=["GET", "POST"])
def apiUsuario():
    logged_in = session.get("logged_in")

    if logged_in:
        data = {
            "username": session.get("username"),
            "name": session.get("name"),
            "email": session.get("email"),
            "profile_picture": session.get("profile_picture"),
        }
        return success_response(data)
    else:
        return error_response("no user logged")


@api_usuarios_blueprint.route("/api/login", methods=["POST"])
def apiLogin():
    r = request.get_json()
    username = r.get("username")
    password = r.get("password")

    success, user = checkUsuario(username, password)

    if success:
        update_session(session, user)
        return success_response()
    else:
        return error_response("Usuario e/ou senha incorreta")


@api_usuarios_blueprint.route("/api/logout", methods=["POST"])
@is_logged_in
def apiLogout():
    session.clear()
    return success_response()


@api_usuarios_blueprint.route("/api/cadastro/usuario", methods=["POST"])
def apiCadastroUsuario():
    r = request.get_json()
    success, message = cadastroUsuario(r)

    if success:
        return success_response()
    else:
        return error_response(message)


@api_usuarios_blueprint.route("/api/update/usuario", methods=["POST"])
def apiUpdateUsuario():
    r = request.get_json()
    id_user = session.get("id")
    success, message = updateUsuario(id_user, r)

    if success:
        update_session(session, getUsuario(id_user=id_user)[1])
        return success_response()
    else:
        return error_response(message)
