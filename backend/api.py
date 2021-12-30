from backend import db
from backend.utils.utils import sanitizeString
from backend.models import (
    Arquivos,
    Disciplinas,
    Users,
    Mamao,
    Penoso,
    Gostei,
    NaoGostei,
    Comentario,
    Links,
)
from backend.views import (
    ArquivosInformacoes,
    DisciplinasInformacoes,
    ComentariosInformacoes,
    LinksInformacoes,
    AvaliacoesDisciplinas,
    AvaliacoesComentario,
)
import traceback
from passlib.hash import sha256_crypt
from io import BytesIO
from base64 import b64decode


def getDisciplinas():
    disciplinas = Disciplinas.query.all()
    sorted_disciplinas = sorted(
        [d.serialize() for d in disciplinas], key=lambda x: x["nome"]
    )
    return sorted_disciplinas


def getDisciplina(id_disciplina: int):
    disciplina = DisciplinasInformacoes.query.filter_by(id=id_disciplina).first()
    return disciplina.serialize() if disciplina else {}


def cadastroUsuario(data):
    name = data.get("name")
    email = data.get("email")
    username = data.get("username")
    picture = data.get("picture", "")
    password = sha256_crypt.encrypt(str(data.get("password")))

    r = Users.query.filter_by(username=username).first()
    if r:
        return False, "Username já cadastrado"
    r = Users.query.filter_by(email=email).first()
    if r:
        return False, "Email já cadastrado"

    novo_usuario = Users(
        name=name, email=email, username=username, picture=picture, password=password
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return True, None


def getUsuario(**kwargs):
    message = "user not found"
    if kwargs.get("user"):
        user = kwargs.get("user")
        user_dict = user.serialize()
        user_dict["password"] = ""
        return True, user_dict
    elif kwargs.get("id_user"):
        id_user = kwargs.get("id_user")
        user = Users.query.filter_by(id=id_user).first()
        if user:
            user_dict = user.serialize()
            user_dict["password"] = ""
            return True, user_dict
        else:
            return False, message
    else:
        return False, message


def checkUsuario(username, passwordEntered):
    user = Users.query.filter_by(username=username).first()

    if user:
        correctPassword = user.password
        # compare hash with entered hash
        if sha256_crypt.verify(passwordEntered, correctPassword):
            return True, getUsuario(user=user)[1]

    return False, None


def updateUsuario(id_user, data):
    name = data.get("name")
    picture = data.get("profile_picture", "")
    password = data.get("password")

    new_data = {
        "name": name,
        "picture": picture,
    }

    if password:
        new_data.update({"password": sha256_crypt.encrypt(str(password))})

    try:
        Users.query.filter_by(id=id_user).update(new_data)
        db.session.commit()
        return True, None

    except Exception as e:
        return False, str(e)


def cadastroAvaliacaoDisciplina(categoria, id_disciplina, id_user):
    try:
        id_user = int(id_user)
        r = AvaliacoesDisciplinas.query.filter_by(
            id_disciplina=id_disciplina, id_user=id_user
        ).first()
        if r:
            return False, "Voce ja avaliou essa disciplina"

        if categoria == "mamao":
            nova_avaliacao = Mamao(id_disciplina=id_disciplina, id_user=id_user)
        else:
            nova_avaliacao = Penoso(id_disciplina=id_disciplina, id_user=id_user)

        db.session.add(nova_avaliacao)
        db.session.commit()
        return True, None

    except Exception as e:
        print(e)
        return False, "Um ocorreu enquanto processava"


def cadastroAvaliacaoComentario(id_comentario, categoria, id_user):
    try:
        id_user = int(id_user)
        r = AvaliacoesComentario.query.filter_by(
            id_comentario=id_comentario, id_user=id_user
        ).first()
        if r:
            return False, "Voce ja avaliou esse comentario"

        if categoria == "gostei":
            nova_avaliacao = Gostei(id_comentario=id_comentario, id_user=id_user)
        else:
            nova_avaliacao = NaoGostei(id_comentario=id_comentario, id_user=id_user)

        db.session.add(nova_avaliacao)
        db.session.commit()
        return True, None

    except Exception as e:
        print(e)
        return False, "ocorreu um erro enquanto processava"


def cadastroDisciplina(nome, penoso_mamao, id_user):
    try:
        nome_limpo = " ".join([sanitizeString(x) for x in nome.split(" ")])
        id_user = int(id_user)

        r = Disciplinas.query.filter_by(nome_limpo=nome_limpo).first()
        if r:
            return False, "Disciplina ja cadastrada"

        nova_disciplina = Disciplinas(id_user=id_user, nome=nome, nome_limpo=nome_limpo)
        db.session.add(nova_disciplina)
        db.session.commit()
        return cadastroAvaliacaoDisciplina(penoso_mamao, nova_disciplina.id, id_user)

    except Exception as e:
        print(e)
        return False, "ocorreu um erro enquanto processava"


def cadastroComentario(id_user, id_disciplina, texto):
    try:
        id_user = int(id_user)
        novo_comentario = Comentario(
            id_user=id_user, id_disciplina=id_disciplina, texto=texto
        )
        db.session.add(novo_comentario)
        db.session.commit()
        return True, None

    except Exception as e:
        print(e)
        return False, "ocorreu um erro enquanto processava"


def cadastroLink(id_user, id_disciplina, titulo, link):
    try:
        id_user = int(id_user)
        novo_link = Links(
            id_user=id_user, id_disciplina=id_disciplina, titulo=titulo, link=link
        )
        db.session.add(novo_link)
        db.session.commit()
        return True, None

    except Exception as e:
        print(e)
        return False, "ocorreu um erro enquanto processava"


def cadastro_arquivo(id_user, id_disciplina, nome, mimetype, descricao, dados):
    try:
        id_user = int(id_user)
        novo_arquivo = Arquivos(
            id_user=id_user,
            id_disciplina=id_disciplina,
            nome=nome.strip(),
            mimetype=mimetype,
            descricao=descricao,
            dados=dados.encode("ascii")
        )
        db.session.add(novo_arquivo)
        db.session.commit()
        return True, None

    except Exception:
        traceback.print_exc()
        return False, "ocorreu um erro enquanto processava"


def getComentarios(id_disciplina=None):
    if id_disciplina:
        comentarios = ComentariosInformacoes.query.filter_by(
            id_disciplina=id_disciplina
        ).all()
    else:
        comentarios = ComentariosInformacoes.query.all()

    if comentarios:
        sort_comentarios = sorted(
            [c.serialize() for c in comentarios], key=lambda x: x["id_comentario"]
        )
        value = sort_comentarios
    else:
        value = comentarios

    return value


def getLinks(id_disciplina=None):
    if id_disciplina:
        links = LinksInformacoes.query.filter_by(id_disciplina=id_disciplina).all()
    else:
        links = LinksInformacoes.query.all()

    if links:
        sorted_links = sorted(
            [link.serialize() for link in links], key=lambda x: x["id_link"]
        )
        value = sorted_links
    else:
        value = links

    return value


def get_arquivos_informacoes(id_disciplina: int):
    arquivos = ArquivosInformacoes.query.filter_by(id_disciplina=id_disciplina).all()
    if arquivos:
        return sorted(
            [arquivo.serialize() for arquivo in arquivos], key=lambda x: x["id_arquivo"]
        )
    return []


def get_arquivo(id_arquivo: int):
    arquivo = Arquivos.query.filter_by(id=id_arquivo).first()
    if arquivo:
        serialized_arquivo = arquivo.serialize()
        serialized_arquivo["dados"] = BytesIO(b64decode(serialized_arquivo["dados"]))
        return serialized_arquivo
    return {}


def getTopDisciplinas(n, categoria):
    TIPOS = ["mamao", "penoso"]

    disciplinas = DisciplinasInformacoes.query.all()
    disciplinas = [d.serialize() for d in disciplinas]

    if categoria not in TIPOS:
        return {}

    for disciplina in disciplinas:
        disciplina["razao"] = disciplina["num_mamao"] / (
            disciplina["num_mamao"] + disciplina["num_penoso"]
        )
        disciplina["num_votos"] = disciplina["num_mamao"] + disciplina["num_penoso"]

    reverse = True if categoria == "mamao" else False

    sorted_disciplinas = sorted(disciplinas, key=lambda x: x["razao"], reverse=reverse)

    size = min(n, len(sorted_disciplinas))

    return sorted_disciplinas[:size]


def deletarComentario(id_comentario, username):

    try:
        r = ComentariosInformacoes.query.filter_by(
            id_comentario=id_comentario, username=username
        ).first()

        if r is None:
            print("Voce nao escreveu este comentario")
            return False, "Voce nao escreveu este comentario"

        else:
            Gostei.query.filter_by(id_comentario=id_comentario).delete()
            NaoGostei.query.filter_by(id_comentario=id_comentario).delete()

            Comentario.query.filter_by(id=id_comentario).delete()
            db.session.commit()

            return True, "Comentario removido com sucesso"

    except Exception as e:
        print(e)
        return False, "ocorreu um erro enquanto processava"
