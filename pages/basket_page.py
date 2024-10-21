
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class BasketPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    submit_button = '//input[@name="submit"]'


    # Getters
    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.submit_button)))

    # Actions
    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")



    def submit_order(self):
        self.get_current_url()
        self.click_submit_button()