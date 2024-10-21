import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.basket_page import BasketPage
from pages.computers_page import ComputersPage
from pages.main_page import MainPage
from pages.monitor_huawei_page import MonitorsHuaweiPage
from pages.monitors_page import MonitorsPage
from pages.order_page import OrderPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start test')

    login = MainPage(driver)
    login.authorization()
    login.select_category()
    computers = ComputersPage(driver)
    computers.click_monitors()
    monitors = MonitorsPage(driver)
    monitors.product_selection()
    buy_monitor = MonitorsHuaweiPage(driver)
    buy_monitor.buy_monitor()
    submit_order = BasketPage(driver)
    submit_order.submit_order()
    finish_order = OrderPage(driver)
    finish_order.submit_order()

    time.sleep(3)
    driver.close()