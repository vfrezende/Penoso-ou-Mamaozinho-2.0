from backend import db
from backend.utils.decorators import serializable_class


@serializable_class
class DisciplinasInformacoes(db.Model):
    __table__ = db.Table(
        "disciplinas_informacoes",
        db.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("nome", db.String()),
        db.Column("nome_limpo", db.String()),
        db.Column("num_mamao", db.Integer),
        db.Column("num_penoso", db.Integer),
        db.Column("num_comentarios", db.Integer),
        autoload=True,
        autoload_with=db.engine,
    )


@serializable_class
class ComentariosInformacoes(db.Model):
    __table__ = db.Table(
        "comentarios_informacoes",
        db.metadata,
        db.Column("id_comentario", db.Integer, primary_key=True),
        db.Column("id_disciplina", db.Integer),
        db.Column("texto", db.String()),
        db.Column("picture", db.String()),
        db.Column("username", db.String()),
        db.Column("num_gostei", db.Integer),
        db.Column("num_nao_gostei", db.Integer),
        autoload=True,
        autoload_with=db.engine,
    )


@serializable_class
class LinksInformacoes(db.Model):
    __table__ = db.Table(
        "links_informacoes",
        db.metadata,
        db.Column("id_link", db.Integer, primary_key=True),
        db.Column("id_disciplina", db.Integer),
        db.Column("titulo", db.String()),
        db.Column("link", db.String()),
        db.Column("picture", db.String()),
        db.Column("username", db.String()),
        autoload=True,
        autoload_with=db.engine,
    )


@serializable_class
class ArquivosInformacoes(db.Model):
    __table__ = db.Table(
        "arquivos_informacoes",
        db.metadata,
        db.Column("id_arquivo", db.Integer, primary_key=True),
        db.Column("id_disciplina", db.Integer),
        db.Column("nome", db.String()),
        db.Column("descricao", db.String()),
        db.Column("mimetype", db.String()),
        db.Column("picture", db.String()),
        db.Column("username", db.String()),
        autoload=True,
        autoload_with=db.engine,
    )


@serializable_class
class AvaliacoesDisciplinas(db.Model):
    __table__ = db.Table(
        "avaliacoes_disciplinas",
        db.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("id_disciplina", db.Integer),
        db.Column("id_user", db.Integer),
        db.Column("categoria", db.String()),
        autoload=True,
        autoload_with=db.engine,
    )


@serializable_class
class AvaliacoesComentario(db.Model):
    __table__ = db.Table(
        "avaliacoes_comentario",
        db.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("id_comentario", db.Integer),
        db.Column("id_user", db.Integer),
        autoload=True,
        autoload_with=db.engine,
    )
