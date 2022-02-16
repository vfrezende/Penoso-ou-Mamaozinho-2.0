from unittest import TestCase
from tests.e2e_tests.account.account_scenarios import AccountScenarios


class TestAccount(TestCase):

    def setUp(self):
        self.given_ = self.when_ = self.then_ = self.and_ = self.scenario_ = \
            AccountScenarios(self.assertEqual, self.assertDictEqual)

    def test_new_users_should_be_able_to_create_a_new_account(self):
        self.given_.user_has_valid_credentials()
        self.when_.user_tries_to_create_a_new_account()
        self.and_.wait_a_few_seconds()
        self.then_.user_should_be_notified_about_created_account()
        self.and_.new_account_should_be_created_in_database()

    def test_new_users_should_not_be_able_to_create_a_account_with_an_already_registered_email(self):
        self.given_.user_has_valid_credentials()
        self.and_.there_is_a_user_with_the_same_email()
        self.when_.user_tries_to_create_a_new_account()
        self.and_.wait_a_few_seconds()
        self.then_.user_should_be_notified_about_already_registered_email()
        self.and_.new_account_should_not_be_created_in_database()

    def tearDown(self):
        self.scenario_.clean_up()
