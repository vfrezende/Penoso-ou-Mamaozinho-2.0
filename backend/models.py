from backend import db
from backend.utils.decorators import serializable_class

from sqlalchemy.types import LargeBinary


@serializable_class
class Comentario(db.Model):
    __tablename__ = "comentario"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    id_disciplina = db.Column(db.Integer)
    texto = db.Column(db.String())

    def __init__(self, id_user, id_disciplina, texto):
        self.id_user = id_user
        self.id_disciplina = id_disciplina
        self.texto = texto


@serializable_class
class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())
    picture = db.Column(db.String())

    def __init__(self, name, email, username, password, picture):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.picture = picture


@serializable_class
class Disciplinas(db.Model):
    __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    nome = db.Column(db.String())
    nome_limpo = db.Column(db.String())

    def __init__(self, id_user, nome, nome_limpo):
        self.id_user = id_user
        self.nome = nome
        self.nome_limpo = nome_limpo


@serializable_class
class Gostei(db.Model):
    __tablename__ = "gostei"

    id = db.Column(db.Integer, primary_key=True)
    id_comentario = db.Column(db.Integer)
    id_user = db.Column(db.Integer)

    def __init__(self, id_comentario, id_user):
        self.id_comentario = id_comentario
        self.id_user = id_user


@serializable_class
class NaoGostei(db.Model):
    __tablename__ = "nao_gostei"

    id = db.Column(db.Integer, primary_key=True)
    id_comentario = db.Column(db.Integer)
    id_user = db.Column(db.Integer)

    def __init__(self, id_comentario, id_user):
        self.id_comentario = id_comentario
        self.id_user = id_user


@serializable_class
class Links(db.Model):
    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer)
    id_user = db.Column(db.Integer)
    titulo = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self, id_disciplina, id_user, titulo, link):
        self.id_disciplina = id_disciplina
        self.id_user = id_user
        self.titulo = titulo
        self.link = link


@serializable_class
class Mamao(db.Model):
    __tablename__ = "mamao"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer)
    id_user = db.Column(db.Integer)

    def __init__(self, id_disciplina, id_user):
        self.id_disciplina = id_disciplina
        self.id_user = id_user


@serializable_class
class Penoso(db.Model):
    __tablename__ = "penoso"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer)
    id_user = db.Column(db.Integer)

    def __init__(self, id_disciplina, id_user):
        self.id_disciplina = id_disciplina
        self.id_user = id_user


@serializable_class
class DenunciaComentario(db.Model):
    __tablename__ = "denuncias"

    id = db.Column(db.Integer, primary_key=True)
    id_comentario = db.Column(db.Integer)
    id_user = db.Column(db.Integer)

    def __init__(self, id_comentario, id_user):
        self.id_comentario = id_comentario
        self.id_user = id_user


@serializable_class
class Arquivos(db.Model):
    __tablename__ = "arquivos"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer)
    id_user = db.Column(db.Integer)
    nome = db.Column(db.String())
    mimetype = db.Column(db.String())
    descricao = db.Column(db.String())
    dados = db.Column(LargeBinary)

    def __init__(self, id_disciplina, id_user, nome, mimetype, descricao, dados):
        self.id_disciplina = id_disciplina
        self.id_user = id_user
        self.nome = nome
        self.mimetype = mimetype
        self.descricao = descricao
        self.dados = dados
