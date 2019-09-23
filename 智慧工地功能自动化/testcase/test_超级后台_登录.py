# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page import loginPage
import time
import unittest
from page.loginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
from generator import *

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = LoginPage(self.driver)
        self.page.get(self.url)
        self.username = username['iotrack']
        self.password = password['iotrack']

    def tearDown(self):
        self.driver.close()

    def test_1_登录(self):
        """
        登录
        :return:
        """

        self.page.username.clear()
        self.page.username = self.username
        self.page.password = self.password

        self.page.login.click()
        time.sleep(2)

        self.assertEqual(self.page.page_url,self.driver.current_url)

    def test_2_退出(self):
        """
        登出
        :return:
        """
        self.page.username.clear()
        self.page.username = self.username
        self.page.password = self.password

        self.page.login.click()
        time.sleep(2)

        self.assertEqual(self.page.page_url,self.driver.current_url)

        move = self.driver.find_element_by_xpath(self.page.image)
        ActionChains(self.driver).move_to_element(move).perform()
        time.sleep(2)

        # 点击退出
        self.page.quit.click()
        time.sleep(2)

        # 断言
        self.assertEqual(self.driver.current_url,self.page.home_url)

if __name__ == '__main__':
    unittest.main()

