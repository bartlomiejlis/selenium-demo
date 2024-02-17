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
        pass
