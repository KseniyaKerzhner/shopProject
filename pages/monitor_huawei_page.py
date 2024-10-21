
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MonitorsHuaweiPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    buy_button = '//a[contains(text(), "Купить")]'
    order_button = '//a[contains(text(), "Оформить заказ")]'

    # Getters
    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.buy_button)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.order_button)))




    # Actions
    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click buy button")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")



    def buy_monitor(self):
        self.get_current_url()
        self.assert_url('https://www.onlinetrade.ru/catalogue/monitory-c23/huawei/monitor_huawei_mateview_gt_27_xwu_cba_black_53060446-2962266.html')
        self.click_buy_button()
        self.click_order_button()
