from locators.locators import MyAccountLocators
from selenium.webdriver.common.by import By


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.addresses_link_text = MyAccountLocators.addresses_link_text

    def addresses_open(self):
        self.driver.find_element(By.LINK_TEXT, self.addresses_link_text).click()
