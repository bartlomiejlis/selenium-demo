class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.addresses_link_text = 'Addresses'

    def addresses_open(self):
        self.driver.find_element(By.LINK_TEXT, self.addresses_link_text).click()
