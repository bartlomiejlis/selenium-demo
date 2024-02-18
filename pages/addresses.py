class AddressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.edit_link_text = 'Edit'

    def edit_open(self):
        self.driver.find_element(By.LINK_TEXT, self.edit_link_text).click()
