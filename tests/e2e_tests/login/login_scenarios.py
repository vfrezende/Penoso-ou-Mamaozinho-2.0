from passlib.hash import sha256_crypt
from selenium.webdriver.common.by import By

from tests.e2e_tests.base_scenario import BaseScenario
from tests.e2e_tests.helpers.database import DatabaseHelper
from tests.e2e_tests.test_utils import Paths

INVALID_ACCOUNT_MESSAGE = 'Usuario e/ou senha incorreta'


class LoginScenarios(BaseScenario):

    def __init__(self, assert_equal):
        super().__init__()

        self.assert_equal = assert_equal

        self.db_helper = DatabaseHelper()

        self.home_url = self.base_url + Paths.HOME_PATH
        self.login_url = self.base_url + Paths.LOGIN_PATH

        self.user = None
        self.password = None

    # Given
    def user_has_a_valid_account(self):
        self.user = self.build_random_user()
        self.password = self.user.password
        self.user.password = sha256_crypt.hash(self.user.password)
        self.db_helper.create_account(self.user)

    def user_has_a_invalid_account(self):
        self.user = self.build_random_user()
        self.password = self.user.password

    # When
    def user_tries_to_login(self):
        self.driver.get(self.login_url)

        self.driver.find_element(By.ID, 'username').send_keys(self.user.username)
        self.driver.find_element(By.ID, 'password').send_keys(self.password)

        self.driver.find_element(By.CSS_SELECTOR, 'input.button').click()

    # Then
    def user_should_be_redirect_to_homepage(self):
        self.assert_equal(self.driver.current_url, self.home_url)

    def user_should_not_be_redirect(self):
        self.assert_equal(self.driver.current_url, self.login_url)

    def user_should_be_notified(self):
        message = self.driver.find_element(By.CSS_SELECTOR, 'div.alert').text
        self.assert_equal(message, INVALID_ACCOUNT_MESSAGE)

    # Scenario
    def clean_up(self):
        print('Limpando dados da execução')
        if self.user:
            self.db_helper.remove_account(self.user.username)
