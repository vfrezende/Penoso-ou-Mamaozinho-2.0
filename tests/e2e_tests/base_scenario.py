from time import sleep
from selenium import webdriver

from tests.e2e_tests.test_utils import User, build_random_string_with_prefix,\
    build_random_string_with_suffix

# Must use the host IP from docker network
BASE_URL = 'http://localhost:5000'
A_FEW_SECONDS = 5


class BaseScenario:

    def __init__(self):
        self._setup_driver()
        self.base_url = BASE_URL

    def _setup_driver(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.implicitly_wait(A_FEW_SECONDS)

    # Utils
    @staticmethod
    def wait_a_few_seconds():
        sleep(A_FEW_SECONDS)

    @staticmethod
    def build_random_user(email: str = build_random_string_with_suffix('@email.com')):
        return User(
            name=build_random_string_with_prefix('name'),
            email=email,
            username=build_random_string_with_prefix('username'),
            password=build_random_string_with_prefix('password'),
            picture=BaseScenario.build_random_url(),
        )

    @staticmethod
    def build_random_url() -> str:
        return f'https://{build_random_string_with_prefix("url")}.com'
