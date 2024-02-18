class BillingAddressEditPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_id = 'billing_first_name'
        self.last_name_id = 'billing_last_name'
        self.country_id = 'billing_country'
        self.street_address_id_1 = 'billing_address_1'
        self.street_address_id_2 = 'billing_address_2'
        self.postcode_id = 'billing_postcode'
        self.city_id = 'billing_city'
        self.phone_id = 'billing_phone'
        self.save_address_btn_name = 'save_address'

    def set_first_name(self, first_name):
        self.driver.find_element('id', self.first_name_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element('id', self.last_name_id).send_keys(last_name)

    def set_country(self, country):
        self.Select(self.driver.find_element('id', self.country_id).select_by_visible_text(country))

    def set_street_address(self, street, apartment):
        self.driver.find_element('id', self.street_address_id_1).send_keys(street)
        self.driver.find_element('id', self.street_address_id_2).send_keys(apartment)

    def set_postcode(self, postcode):
        self.driver.find_element('id', self.postcode_id).send_keys(postcode)

    def set_city(self, city):
        self.driver.find_element('id', self.city_id).send_keys(city)

    def set_phone_num(self,phone_num):
        self.driver.find_element('id', self.phone_id).send_keys(phone_num)

    def save_address(self):
        self.driver.find_element('name', self.save_address_btn_name).send_keys(Keys.ENTER)
