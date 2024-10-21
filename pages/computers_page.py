from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ComputersPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    monitors = '//a[@title="Мониторы"]'

    # Getters
    def get_monitors(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.monitors)))

    # Actions
    def click_monitors(self):
        self.get_current_url()
        self.assert_url('https://www.onlinetrade.ru/catalogue/kompyutery_i_periferiya-c243/')
        self.get_monitors().click()
        print("Click monitors button")