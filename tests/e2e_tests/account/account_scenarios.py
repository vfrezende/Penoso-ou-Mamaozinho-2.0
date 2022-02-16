from dataclasses import asdict
from selenium.webdriver.common.by import By
from tests.e2e_tests.test_utils import User

from tests.e2e_tests.base_scenario import BaseScenario
from tests.e2e_tests.helpers.database import DatabaseHelper
from tests.e2e_tests.test_utils import Paths, build_random_string_with_prefix, build_random_string_with_suffix

SUCCESS_MESSAGE = "Registrado com Sucesso!"
EMAIL_ALREADY_REGISTERED_MESSAGE = "Email já cadastrado"


class AccountScenarios(BaseScenario):

    def __init__(self, assert_equal, assert_dict_equal):
        super().__init__()

        self.assert_equal = assert_equal
        self.assert_dict_equal = assert_dict_equal

        self.db_helper = DatabaseHelper()

        self.register_url = self.base_url + Paths.REGISTER_PATH
        self.login_url = self.base_url + Paths.LOGIN_PATH

        self.user = None
        self.aux_user = None

    # Given
    def user_has_valid_credentials(self):
        self.user = User(
            name=build_random_string_with_prefix('name'),
            email=build_random_string_with_suffix('@email.com'),
            username=build_random_string_with_prefix('username'),
            password=build_random_string_with_prefix('password'),
            picture=self._build_random_url(),
        )

    def there_is_a_user_with_the_same_email(self):
        self.aux_user = User(
            name=build_random_string_with_prefix('name'),
            email=self.user.email,
            username=build_random_string_with_prefix('username'),
            password=build_random_string_with_prefix('password'),
            picture=self._build_random_url(),
        )
        self.db_helper.create_account(self.aux_user)

    # When
    def user_tries_to_create_a_new_account(self):
        self.db_helper.remove_account(self.user.username)

        self.driver.get(self.register_url)

        self.driver.find_element(By.ID, 'name').send_keys(self.user.name)
        self.driver.find_element(By.ID, 'email').send_keys(self.user.email)
        self.driver.find_element(By.ID, 'username').send_keys(self.user.username)
        self.driver.find_element(By.ID, 'picture').send_keys(self.user.picture)
        self.driver.find_element(By.ID, 'password').send_keys(self.user.password)
        self.driver.find_element(By.ID, 'confirm').send_keys(self.user.password)

        self.driver.find_element(By.CSS_SELECTOR, '#register button').click()

    # Then
    def user_should_be_notified_about_created_account(self):
        received_message = self.driver.find_element(By.CSS_SELECTOR, '.alert-success').text
        self.assert_equal(SUCCESS_MESSAGE, received_message)

    def user_should_be_notified_about_already_registered_email(self):
        received_message = self.driver.find_element(By.CSS_SELECTOR, '.alert-danger').text
        self.assert_equal(EMAIL_ALREADY_REGISTERED_MESSAGE, received_message)

    def new_account_should_be_created_in_database(self):
        received_user = self.db_helper.get_account(self.user.username)

        user_asdict = asdict(self.user)
        user_asdict['password'] = received_user.password
        user_asdict['id'] = received_user.id

        self.assert_dict_equal(received_user.serialize(), user_asdict)

    def new_account_should_not_be_created_in_database(self):
        received_user = self.db_helper.get_account(self.user.username)

        self.assert_equal(received_user, None)

    # Utils
    def _build_random_url(self) -> str:
        return f'https://{build_random_string_with_prefix("url")}.com'

    # Scenario
    def clean_up(self):
        print('Limpando dados da execução')
        if self.user:
            self.db_helper.remove_account(self.user.username)
        if self.aux_user:
            self.db_helper.remove_account(self.aux_user.username)
        self.db_helper.clean_up()
