import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        login_register_page.create_account('mojenowekonto@wp.pl', 'mojenowehaslo')

        assert self.driver.find_element(By.LINK_TEXT, 'Logout').is_displayed()

    def test_register_fail(self, setup):
        self.driver.get('http://seleniumdemo.com/?page_id=7')
        login_register_page = LoginRegisterPage(self.driver)
        login_register_page.create_account('mojenowekonto@wp.pl', 'mojenowehaslo')

        msg = "Error: An account is already registered with your email address. Please log in"

        assert msg in self.driver.find_element('xpath', "//ul[@class='woocommerce-error']").text

    def test_log_in_pass(self, setup):
        self.driver.get('http://seleniumdemo.com/?page_id=7')
        login_register_page = LoginRegisterPage(self.driver)
        login_register_page.login('mojenowekonto@wp.pl', 'mojenowehaslo')

        assert self.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    def test_log_in_fail(self, setup):
        self.driver.get('http://seleniumdemo.com/?page_id=7')
        login_register_page = LoginRegisterPage(self.driver)
        # Passing login data of non-existent account
        login_register_page.login('mojestarekonto@wp.pl', 'mojestarehaslo')

        msg = 'ERROR: Incorrect username or password.'

        assert msg in self.driver.find_element('xpath', "//ul[@class='woocommerce-error']").text

    def test_update_address(self, setup):
        self.driver.get('http://seleniumdemo.com/?page_id=7')

        email = str(random.randint(0, 1000)) + 'testowymail@wp.pl'

        login_register_page = LoginRegisterPage(self.driver)
        login_register_page.create_account(email, 'fajnenowehaslo')

        my_account_page = MyAccountPage(self.driver)
        my_account_page.addresses_open()

        addresses_page = AddressesPage(self.driver)
        addresses_page.edit_open()

        # Filling the form
        billing_address_edit_page = BillingAddressEditPage(self.driver)
        billing_address_edit_page.set_first_name('Jan')
        billing_address_edit_page.set_last_name('Kowalski')
        billing_address_edit_page.set_country('Poland')
        billing_address_edit_page.set_street_address('Zwycięstwa 1', '23')
        billing_address_edit_page.set_postcode('12-345')
        billing_address_edit_page.set_city('Warsaw')
        billing_address_edit_page.set_phone_num('+48 123 456 789')
        billing_address_edit_page.save_address()

        msg = 'Address changed successfully.'

        assert msg in self.driver.find_element('xpath', "//div[@class='woocommerce-message']").text
