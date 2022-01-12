from backend.utils.decorators import is_logged_in
from mock import patch, MagicMock
from unittest import TestCase

LOGGED_IN = "logged_in"
PAGE_TO_REDIRECT = "views.views-home.unauthorized"


@patch("backend.utils.decorators.flask")
class TestDecorators(TestCase):

    def setUp(self):
        self.func = MagicMock()
        self.func_wrapped_is_logged_in = is_logged_in(self.func)

    def test_is_logged_in_should_return_wrapped_function_when_user_is_logged_in(self, flask_mock):
        flask_mock.session = self._mock_session_with_value(True)

        self.assertEqual(self.func_wrapped_is_logged_in(), self.func())

    def test_is_logged_in_should_redirect_when_user_is_not_logged_in(self, flask_mock):
        flask_mock.session = self._mock_session_with_value(False)
        flask_mock.redirect = MagicMock()
        flask_mock.url_for = MagicMock()

        _ = self.func_wrapped_is_logged_in()

        flask_mock.url_for.assert_called_once_with(PAGE_TO_REDIRECT)
        flask_mock.redirect.assert_called_once_with(flask_mock.url_for.return_value)

    @staticmethod
    def _mock_session_with_value(value):
        return {
            LOGGED_IN: value,
        }
