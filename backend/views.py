from backend import db


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

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nome_limpo": self.nome_limpo,
            "num_mamao": self.num_mamao,
            "num_penoso": self.num_penoso,
            "num_comentarios": self.num_comentarios,
        }


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

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id_comentario": self.id_comentario,
            "id_disciplina": self.id_disciplina,
            "texto": self.texto,
            "picture": self.picture,
            "username": self.username,
            "num_gostei": self.num_gostei,
            "num_nao_gostei": self.num_nao_gostei,
        }


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

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id_link": self.id_link,
            "id_disciplina": self.id_disciplina,
            "titulo": self.titulo,
            "link": self.link,
            "picture": self.picture,
            "username": self.username,
        }


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

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "id_disciplina": self.id_disciplina,
            "id_user": self.id_user,
            "categoria": self.categoria,
        }


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

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "id_comentario": self.id_comentario,
            "id_user": self.id_user,
        }
