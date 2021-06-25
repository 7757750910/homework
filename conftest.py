import logging

from selenium import webdriver


class TestSelenium:
    def setup(self):
        logging.info('设置浏览器驱动，窗口最大化，隐形等待设置为5s')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
