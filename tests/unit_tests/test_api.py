from mock.mock import MagicMock
from backend.api import cadastro_arquivo, deletarComentario, denunciarComentario

from random import randint
from unittest import TestCase
from mock import patch


@patch("backend.api.views")
@patch("backend.api.models")
@patch("backend.api.db")
class TestApi(TestCase):

    def test_cadastro_arquivo_deve_salvar_arquivo_novo_arquivo_corretamente(
        self, db_mock, models_mock, views_mock):

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

    def test_denunciar_comentario_nao_deve_permitir_um_usuario_denunciar_mais_de_uma_vez_um_comentario(
        self, db_mock, models_mock, views_mock):

        id_user = str(randint(1, 100))
        id_comentario = randint(1, 100)

        self._mock_denuncia_comentario_query(models_mock, return_value=MagicMock())

        success, message = denunciarComentario(id_comentario, id_user)

        db_mock.session.add.assert_not_called()
        db_mock.session.commit.assert_not_called()
        self.assertEqual(success, False)
        self.assertEqual(message, "Voce ja denunciou este comentario")

    def test_denunciar_comentario_deve_remover_comentario_na_quinta_denuncia(
        self, db_mock, models_mock, views_mock):

        id_user = str(randint(1, 100))
        id_comentario = randint(1, 100)

        self._mock_denuncia_comentario_query(models_mock, return_value=None, n=5)

        success, message = denunciarComentario(id_comentario, id_user)

        models_mock.DenunciaComentario.has_any_call(id_comentario, id_user)
        db_mock.session.add.assert_called_once_with(models_mock.DenunciaComentario())

        self.assertEqual(db_mock.session.commit.call_count, 2)
        self.assertEqual(success, True)
        self.assertEqual(message, None)

    def test_denunciar_comentario_deve_registrar_denuncia(
        self, db_mock, models_mock, views_mock):

        id_user = str(randint(1, 100))
        id_comentario = randint(1, 100)

        self._mock_denuncia_comentario_query(models_mock, return_value=None, n=4)
        success, message = denunciarComentario(id_comentario, id_user)

        models_mock.DenunciaComentario.has_any_call(id_comentario, id_user)
        db_mock.session.add.assert_called_once_with(models_mock.DenunciaComentario())
        db_mock.session.commit.assert_called_once()

        self.assertEqual(success, True)
        self.assertEqual(message, None)

    def test_deletar_comentario_deve_negar_requisicoes_de_outros_usuarios(
        self, db_mock, models_mock, views_mock):

        id_comentario = randint(1, 100)
        username = "username"

        self._mock_comentarios_informacoes_query(views_mock, None)

        success, message = deletarComentario(id_comentario, username)

        self.assertEqual(success, False)
        self.assertEqual(message, "Voce nao escreveu este comentario")

    def test_deletar_comentario_deve_remover_um_comentario_corretamente(
        self, db_mock, models_mock, views_mock):

        id_comentario = randint(1, 100)
        username = "username"

        self._mock_comentarios_informacoes_query(views_mock, MagicMock())

        success, message = deletarComentario(id_comentario, username)

        models_mock.Gostei.query.filter_by.assert_called_once()
        models_mock.NaoGostei.query.filter_by.assert_called_once()
        models_mock.Comentario.query.filter_by.assert_called_once()
        db_mock.session.commit.assert_called_once()

        self.assertEqual(success, True)
        self.assertEqual(message, "Comentario removido com sucesso")

    # Utils
    def _mock_denuncia_comentario_query(self, models_mock, return_value, n=0):
        filter_by_result_mock = MagicMock()

        if n:
            result_all_mock = MagicMock()
            result_all_mock.return_value = [MagicMock()] * n
            filter_by_result_mock.all.side_effect = result_all_mock

        result_first_mock = MagicMock()
        result_first_mock.return_value = return_value
        filter_by_result_mock.first.side_effect = result_first_mock

        models_mock.DenunciaComentario.query.filter_by.return_value = filter_by_result_mock

    def _mock_comentarios_informacoes_query(self, views_mock, return_value):
        result_first_mock = MagicMock()
        result_first_mock.return_value = return_value

        filter_by_result_mock = MagicMock()
        filter_by_result_mock.first.side_effect = result_first_mock

        views_mock.ComentariosInformacoes.query.filter_by.return_value = filter_by_result_mock
