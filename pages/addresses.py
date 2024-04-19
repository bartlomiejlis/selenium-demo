from locators.locators import AddressesLocators
from selenium.webdriver.common.by import By


class AddressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.edit_link_text = AddressesLocators.edit_link_text

    def edit_open(self):
        self.driver.find_element(By.LINK_TEXT, self.edit_link_text).click()
