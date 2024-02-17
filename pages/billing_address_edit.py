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
