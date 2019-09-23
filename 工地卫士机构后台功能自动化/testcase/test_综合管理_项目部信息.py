# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.projectloginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
from page.Page_综合管理_项目部信息 import *

phone = []
phone.append(random_phone_number())

class TestProjectLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = DepartmentInfoPage.url
        self.driver.maximize_window()
        self.page = DepartmentInfoPage(self.driver)
        self.page.get(self.url)
        self.username = username.get('project_department')
        self.password = password.get('project_department')
        self.login = ProjectLoginPage(self.driver)

        #*****************************登录*****************************开始
        self.login.username.clear()
        self.login.username = self.username

        self.login.password = self.password

        self.login.login.click()
        time.sleep(2)
        #*****************************登录*****************************结束

        #*****************************切换到账号管理*****************************开始

        self.page.intergrated_management.click()
        time.sleep(2)
        self.page.department_info.click()
        time.sleep(2)

        #*****************************切换到账号管理*****************************结束


    def tearDown(self):
        self.driver.close()



    def test_1_项目部信息编辑(self):
        """
        系统管理-项目部信息-编辑
        :return:
        """

        self.page.department_name = random_company()
        self.page.department_company = random_company()
        self.page.department_code = random_num(18)
        self.page.department_bank = random_address()
        self.page.department_banknum = random_num(15)
        self.page.person_device_code = random_num(15)
        self.page.department_save.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

