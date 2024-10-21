
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MonitorsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    brands_filter_huawei = '//a[@title="HUAWEI"]'
    diagonal_filter_27_29 = '//label[@id="l1d9abad1bde8babc3542e941692d0be8"]'
    show_products = '//a[@class="orange js__filterResult_link"]'
    huawei_mate_view_gt_27 = '//a[contains(text(), "HUAWEI MateView GT 27")]'


    # Getters
    def get_brands_filter_huawei(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.brands_filter_huawei)))

    def get_diagonal_filter_27_29(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.diagonal_filter_27_29)))

    def get_show_products(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.show_products)))

    def get_huawei_mate_view_gt_27 (self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.huawei_mate_view_gt_27 )))


    # Actions
    def click_brands_filter_huawei(self):
        self.get_brands_filter_huawei().click()
        print("Click brand huawei")

    def click_diagonal_filter_27_29(self):
        self.get_diagonal_filter_27_29().click()
        print("Click diagonal filter from 27 to 29.9")

    def click_show_products(self):
        self.get_show_products().click()
        print("Click show products")

    def click_huawei_mate_view_gt_27(self):
        self.get_huawei_mate_view_gt_27().click()
        print("Click show HUAWEI MateView GT 27&quot; XWU-CBA black")


    def product_selection(self):
        self.get_current_url()
        self.assert_url('https://www.onlinetrade.ru/catalogue/monitory-c23/')
        self.click_brands_filter_huawei()
        self.click_diagonal_filter_27_29()
        self.click_huawei_mate_view_gt_27()