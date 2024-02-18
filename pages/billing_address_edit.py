from locators.locators import BillingAddressEditLocators


class BillingAddressEditPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_id = BillingAddressEditLocators.first_name_id
        self.last_name_id = BillingAddressEditLocators.last_name_id
        self.country_id = BillingAddressEditLocators.country_id
        self.street_address_id_1 = BillingAddressEditLocators.street_address_id_1
        self.street_address_id_2 = BillingAddressEditLocators.street_address_id_2
        self.postcode_id = BillingAddressEditLocators.postcode_id
        self.city_id = BillingAddressEditLocators.city_id
        self.phone_id = BillingAddressEditLocators.phone_id
        self.save_address_btn_name = BillingAddressEditLocators.save_address_btn_name

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
