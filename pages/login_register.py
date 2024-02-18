class LoginRegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_address_id = 'reg_email'
        self.re_password_id = 'reg_password'
        self.register_button_name = 'register'
        self.username_id = 'username'
        self.password_id = 'password'
        self.log_in_button_name = 'login'

    def create_account(self, email, password):
        self.driver.find_element('id', self.email_address_id).send_keys(email)
        self.driver.find_element('id', self.re_password_id).send_keys(password)
        self.driver.find_element('name', self.register_button_name).send_keys(Keys.ENTER)

    def login(self, email, password):
        self.driver.find_element('id', self.username_id).send_keys(email)
        self.driver.find_element('id', self.password_id).send_keys(password)
        self.driver.find_element('name', self.log_in_button_name).send_keys(Keys.ENTER)
