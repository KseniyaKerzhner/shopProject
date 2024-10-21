
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class OrderPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    address_textarea = '//textarea[@name="address"]'
    order_button = '//input[@id="order_step2_submit"]'


    # Getters
    def get_address_textarea(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.address_textarea)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.order_button)))

    # Actions
    def input_address_textarea(self, address):
        self.get_address_textarea().send_keys(address)
        print("Input address")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")



    def submit_order(self):
        self.get_current_url()
        self.assert_url('https://www.onlinetrade.ru/basket.html')
        self.input_address_textarea('Ленинградский проспект, дом. 81, кв. 77')
        self.click_order_button()
        self.get_screenshot()