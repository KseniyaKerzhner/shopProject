import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print(f'Current utl: {get_url}')

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Значение url верно")

    def get_screenshot(self):
        """Method for screenshot"""
        now_date = datetime.datetime.now().strftime("_%Y-%m-%d_%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(f'C:\\Users\\k.kerzhner\\PycharmProjects\\shopProject\\screen\\{name_screenshot}')