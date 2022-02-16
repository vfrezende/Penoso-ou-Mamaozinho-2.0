from tests.e2e_tests.base_scenario import BaseScenario
from selenium.webdriver.common.by import By

from tests.e2e_tests.test_utils import Paths

INVALID_ACCOUNT_MESSAGE = 'Usuario e/ou senha incorreta'


class LoginScenarios(BaseScenario):

    def __init__(self, assert_equal):
        super().__init__()

        self.assert_equal = assert_equal

        self.home_url = self.base_url + Paths.HOME_PATH
        self.login_url = self.base_url + Paths.LOGIN_PATH

        self.account_name = None
        self.account_password = None

    # Given
    def user_has_a_valid_account(self):
        self.account_name = 'fseppe'
        self.account_password = '123456'

    def user_has_a_invalid_account(self):
        self.account_name = 'fseppe'
        self.account_password = '1234567'

    # When
    def user_tries_to_login(self):
        self.driver.get(self.login_url)

        self.driver.find_element(By.ID, 'username').send_keys(self.account_name)
        self.driver.find_element(By.ID, 'password').send_keys(self.account_password)

        self.driver.find_element(By.CSS_SELECTOR, 'input.button').click()

    # Then
    def user_should_be_redirect_to_homepage(self):
        self.assert_equal(self.driver.current_url, self.home_url)

    def user_should_not_be_redirect(self):
        self.assert_equal(self.driver.current_url, self.login_url)

    def user_should_be_notified(self):
        message = self.driver.find_element(By.CSS_SELECTOR, 'div.alert').text
        self.assert_equal(message, INVALID_ACCOUNT_MESSAGE)
