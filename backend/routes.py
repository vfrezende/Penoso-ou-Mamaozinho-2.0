from backend import app
from backend.utils.decorators import is_logged_in
from backend.utils.responses import success_response, error_response
from backend.utils.utils import update_session
from backend.api import (
    cadastro_arquivo,
    cadastroComentario,
    cadastroUsuario,
    cadastroDisciplina,
    cadastroLink,
    cadastroAvaliacaoDisciplina,
    cadastroAvaliacaoComentario,
    deletarComentario,
    get_arquivo,
    get_arquivos_informacoes,
    getUsuario,
    updateUsuario,
    getDisciplina,
    getDisciplinas,
    getLinks,
    getComentarios,
    checkUsuario,
    getTopDisciplinas,
    denunciarComentario,
    getAvaliouDisciplina
)
from flask import (
    render_template,
    redirect,
    url_for,
    session,
    request,
    jsonify,
    send_file
)


# index page
@app.route("/")
def index():
    return redirect(url_for("home"))


# Home page
@app.route("/home")
def home():
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


@app.route("/profile")
def profile():
    return render_template("profile.html")


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

    success, user = checkUsuario(username, password)

    if success:
        update_session(session, user)
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


@app.route("/api/arquivos/<int:id_disciplina>",  methods=["GET", "POST"])
@is_logged_in
def api_arquivos(id_disciplina):
    data = get_arquivos_informacoes(id_disciplina)
    return jsonify(data)


@app.route("/api/arquivo/<int:id_arquivo>",  methods=["GET", "POST"])
@is_logged_in
def api_arquivo(id_arquivo):
    arquivo = get_arquivo(id_arquivo)
    return send_file(
        arquivo["dados"],
        mimetype=arquivo["mimetype"],
        attachment_filename=arquivo["nome"],
        as_attachment=True)


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


@app.route("/api/update/usuario", methods=["POST"])
def apiUpdateUsuario():
    r = request.get_json()
    id_user = session.get("id")
    success, message = updateUsuario(id_user, r)

    if success:
        update_session(session, getUsuario(id_user=id_user)[1])
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


@app.route("/api/cadastro/arquivo", methods=["POST"])
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
        id_user,
        id_disciplina,
        nome,
        mimetype,
        descricao,
        dados
    )
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



@app.route("/api/cadastro/denunciar_comentario", methods=["POST"])
@is_logged_in
def apiDenunciarComentario():
    r = request.get_json()

    id_comentario = r.get("id_comentario")
    id_user = session.get("id")

    success, message = denunciarComentario(id_comentario, id_user) 
    print(message)
    if success:
        return success_response()
    else:
        return error_response(message)


@app.route("/api/avaliou_disciplina/<int:id_disciplina>")
@is_logged_in
def apiAvaliouDisciplina(id_disciplina):

    id_user = session.get("id")
    r = getAvaliouDisciplina(id_disciplina, id_user)
    return jsonify(r)

 