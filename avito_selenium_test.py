import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class AvitoPhoneTest(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--start-maximized")
        # self.options.add_argument("--headless")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=self.options, executable_path='chromedriver.exe')
        self.driver.get('https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1')

    def test_avito_login(self):
        # Enter
        self.driver.find_element_by_link_text('Вход и регистрация').click()
        time.sleep(1)
        # login
        login = self.driver.find_element_by_name('login')
        login.send_keys('ваш логин')
        time.sleep(1)
        # password
        login = self.driver.find_element_by_name('password')
        login.send_keys('ваш пароль')
        time.sleep(1)
        # click
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
