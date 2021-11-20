from backend import app
from backend.utils import success_response, error_response
from backend.api import (
    cadastroComentario,
    cadastroUsuario,
    cadastroDisciplina,
    cadastroLink,
    cadastroAvaliacaoDisciplina,
    cadastroAvaliacaoComentario,
    deletarComentario,
)
from backend.api import (
    getDisciplina,
    getDisciplinas,
    getLinks,
    getComentarios,
    checkUsuario,
    getTopDisciplinas,
)

from flask import render_template, redirect, url_for, session, request, jsonify


#
from functools import wraps


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return wrap


# index page
@app.route("/")
def index():
    # create cursor
    return redirect(url_for("home"))


# Home page
@app.route("/home")
def home():
    # create cursor
    return render_template("home.html")


@app.route("/disciplina/<int:id_disciplina>")
@is_logged_in
def disciplina(id_disciplina):
    return render_template("disciplina.html")


@app.route("/adicionar_disciplina")
@is_logged_in
def adicionar_disciplina():
    return render_template("adicionar_disciplina.html")


@app.route("/register")
def cadastro():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    return redirect(url_for("home"))


#  Informacao sobre o usuario da sessao atual
@app.route("/api/usuario", methods=["GET", "POST"])
def apiUsuario():
    print(session)

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


# iniciando sessao apos login do usuario
@app.route("/api/login", methods=["POST"])
def apiLogin():
    r = request.get_json()
    username = r.get("username")
    password = r.get("password")

    status, data = checkUsuario(username, password)

    if status:
        session["logged_in"] = True
        session["id"] = data["id"]
        session["username"] = username
        session["name"] = data["name"]
        session["email"] = data["email"]
        session["profile_picture"] = data["picture"]
        return success_response()
    else:
        return error_response("Usuario e/ou senha incorreta")


@app.route("/api/logout", methods=["POST"])
@is_logged_in
def apiLogout():
    session.clear()
    return success_response()


#               gera lista das disciplinas                  #
# com as respectivas contagens de comentarios e avaliacoes  #
@app.route("/api/disciplinas")
def apiDisciplinas():
    r = getDisciplinas()
    return jsonify(r)


# traz informacoes acerca de uma unica disciplina
@app.route("/api/disciplina/<int:id_disciplina>")
@is_logged_in
def apiDisciplina(id_disciplina):
    r = getDisciplina(id_disciplina)
    return jsonify(r)


# traz os comentarios de uma disciplina
@app.route("/api/comentarios/<int:id_disciplina>")
@is_logged_in
def apiComentarios(id_disciplina):
    data = getComentarios(id_disciplina)
    return jsonify(data)


# traz os comentarios de uma disciplina
@app.route("/api/links/<int:id_disciplina>")
@is_logged_in
def apiLinks(id_disciplina):
    data = getLinks(id_disciplina)
    return jsonify(data)


@app.route("/api/disciplinas/top/<int:n>/<string:categoria>")
def apiTopDisciplinas(n, categoria):
    data = getTopDisciplinas(n, categoria)
    return jsonify(data)


@app.route("/api/cadastro/usuario", methods=["POST"])
def apiCadastroUsuario():
    r = request.get_json()
    success, message = cadastroUsuario(r)

    if success:
        return success_response()
    else:
        return error_response(message)


# cadastra uma nova disciplina
@app.route("/api/cadastro/disciplina", methods=["POST"])
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


# cadastra um novo comentario
@app.route("/api/cadastro/comentario", methods=["POST"])
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


# cadastra um novo link
@app.route("/api/cadastro/link", methods=["POST"])
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


# cadastro uma nova avaliacao de uma disciplina
@app.route("/api/cadastro/avaliacao_disciplina", methods=["POST"])
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


# cadastro uma nova avaliacao de uma disciplina
@app.route("/api/cadastro/avaliacao_comentario", methods=["POST"])
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


@app.route("/api/cadastro/deletar_comentario", methods=["POST"])
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
