# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.organizeloginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *


class TestEditPW(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = LoginPage(self.driver)
        self.page.get(self.url)
        self.username = username.get('organize')
        self.password = password.get('organize')

        self.page.username.clear()
        self.page.username = self.username

        self.page.password = self.password
        # self.page.password = '123456'

        self.page.login.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_1_修改密码(self):
        """
        机构管理员-个人信息-修改密码
        :return:
        """

        move = self.driver.find_element_by_xpath(self.page.image)
        ActionChains(self.driver).move_to_element(move).perform()
        time.sleep(2)

        self.page.info.click()
        time.sleep(2)

        self.page.edit_password.click()
        time.sleep(2)

        self.page.old_password = self.password

        self.page.new_password = self.password
        self.page.confirm_password = self.password

        self.page.edit_save.click()
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()

