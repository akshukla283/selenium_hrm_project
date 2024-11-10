import pytest

from conftest import *
from hrmpages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    @classmethod
    def setup_class(cls):
        cls.driver.get(BaseUrl)
        cls.login_page = LoginPage(cls.driver)

    def test_valid_login(self):
        self.login_page.login(Username, Password)


    def test_valid_login2(self):
        self.login_page.login(Username, Password)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def teardown_method(self):
        self.driver.delete_all_cookies()

