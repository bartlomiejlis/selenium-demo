from locators.locators import LoginRegisterLocators
from selenium.webdriver.common.keys import Keys


class LoginRegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_address_id = LoginRegisterLocators.email_address_id
        self.reg_password_id = LoginRegisterLocators.reg_password_id
        self.register_button_name = LoginRegisterLocators.register_button_name
        self.username_id = LoginRegisterLocators.username_id
        self.password_id = LoginRegisterLocators.password_id
        self.log_in_button_name = LoginRegisterLocators.log_in_button_name

    def create_account(self, email, password):
        self.driver.find_element('id', self.email_address_id).send_keys(email)
        self.driver.find_element('id', self.reg_password_id).send_keys(password)
        self.driver.find_element('name', self.register_button_name).send_keys(Keys.ENTER)

    def login(self, email, password):
        self.driver.find_element('id', self.username_id).send_keys(email)
        self.driver.find_element('id', self.password_id).send_keys(password)
        self.driver.find_element('name', self.log_in_button_name).send_keys(Keys.ENTER)
