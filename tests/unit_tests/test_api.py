from backend.api import cadastro_arquivo

from random import randint
from unittest import TestCase
from mock import patch


@patch("backend.api.views")
@patch("backend.api.models")
@patch("backend.api.db")
class TestApi(TestCase):

    def test_cadastro_arquivo_deve_salvar_arquivo_novo_arquivo_corretamente(self, db_mock, models_mock, views_mock):

        kwargs = {
            "id_user": str(randint(1, 100)),
            "id_disciplina": randint(1, 100),
            "nome": "nome",
            "mimetype": "image/png",
            "descricao": "descricao",
            "dados": "dados",
        }

        cadastro_arquivo(**kwargs)

        kwargs["id_user"] = int(kwargs["id_user"])
        kwargs["dados"] = kwargs["dados"].encode("ascii")

        models_mock.Arquivos.assert_called_once_with(**kwargs)
        db_mock.session.add.assert_called_once_with(models_mock.Arquivos())
        db_mock.session.commit.assert_called_once()
