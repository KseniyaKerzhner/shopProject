
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_button = '//a[@title="Вход в Личный кабинет"]'
    username = '//input[@name="login"]'
    password = '//input[@name="password"]'
    auth_button = '//input[@name="submit"]'
    catalog_button = '//a[@title="Каталог товаров"]'

    computers_category = '//a[@title="Перейти в категорию «Компьютеры и периферия»"]'


    # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.login_button)))

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.password)))

    def get_auth_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.auth_button)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.catalog_button)))

    def get_computers_category(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.computers_category)))

    # Actions
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def input_username(self, username):
        self.get_username().send_keys(username)
        print("Input username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_auth_button(self):
        self.get_auth_button().click()
        print("Click authorization button")

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_computers_category(self):
        self.get_computers_category().click()
        print("Click computers category")



    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_button()
        self.input_username("icy2782@rustyload.com")
        self.input_password("test12345")
        self.click_auth_button()

    def select_category(self):
        self.get_current_url()
        self.click_catalog_button()
        self.click_computers_category()
