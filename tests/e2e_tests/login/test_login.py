from unittest import TestCase

from tests.e2e_tests.login.login_scenarios import LoginScenarios


class TestLogin(TestCase):

    def setUp(self):
        self.given_ = self.when_ = self.then_ = self.and_ = self.scenario_ = \
            LoginScenarios(self.assertEqual)

    def test_when_user_tries_to_login_with_a_valid_account(self):
        self.given_.user_has_a_valid_account()
        self.when_.user_tries_to_login()
        self.and_.wait_a_few_seconds()
        self.then_.user_should_be_redirect_to_homepage()

    def test_when_user_tries_to_login_with_an_invalid_account(self):
        self.given_.user_has_a_invalid_account()
        self.when_.user_tries_to_login()
        self.and_.wait_a_few_seconds()
        self.then_.user_should_not_be_redirect()
        self.and_.user_should_be_notified()

    def tearDown(self):
        self.scenario_.clean_up()
