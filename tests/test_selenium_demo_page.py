import pytest
from selenium import webdriver
from pages.login_register import LoginRegisterPage
from pages.my_account import MyAccountPage
from pages.addresses import AddressesPage
from pages.billing_address_edit import BillingAddressEditPage


class TestSeleniumDemoPage:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_register_pass(self, setup):
        self.driver.get('http://seleniumdemo.com/?page_id=7')
        login_register_page = LoginRegisterPage(self.driver)

