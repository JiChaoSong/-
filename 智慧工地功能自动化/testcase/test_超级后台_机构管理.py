# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page import loginPage
import time
import unittest
from page.organizationPage import *
from page.loginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
import os
from generator import *

path = r'G:\自动化测试脚本\智慧工地功能自动化\testcase\jiaobe.exe'
phone = []
phone.append(random_phone_number())


class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = OrganizePage.url
        self.driver.maximize_window()
        self.page = OrganizePage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)
        self.username = username['iotrack']
        self.password = password['iotrack']

        # 登录
        self.login.username = self.username
        self.login.password = self.password

        self.login.login.click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

    def test_1_新增机构(self):
        """
        机构管理-新增
        :return:
        """

        self.page.add_organize.click()
        time.sleep(2)

        self.page.add_logo.click()
        time.sleep(2)

        os.system(path)
        time.sleep(5)

        self.page.add_organize_name = random_company()
        self.page.add_organize_company = random_company()
        self.page.add_organize_code = random_num(18)
        self.page.add_organize_hangye = random_job()
        self.page.add_organize_starttime = '2019-09-20'
        self.page.add_organize_endtime = '2030-09-20'
        self.page.add_organize_hangye.click()
        self.page.add_organize_num = random_num(3)
        self.page.add_organize_depict = random_sentence()

        self.page.add_organize_person = random_name()
        self.page.add_organize_phone = phone[0]
        time.sleep(3)
        self.page.add_organize_save.click()
        time.sleep(5)


    def test_2_项目配置(self):
        """
        机构管理-项目配置
        :return:
        """

        self.page.search_phone = phone[0]
        self.page.search.click()
        time.sleep(2)

        self.page.project_set.click()
        time.sleep(2)

        self.page.PC.click()
        self.page.APP.click()

        self.page.project_save.click()
        time.sleep(2)


    def test_3_编辑(self):
        """
        机构管理-编辑
        :return:
        """
        self.page.search_phone = phone[0]
        self.page.search.click()
        time.sleep(2)

        self.page.edit.click()
        time.sleep(2)

        self.page.edit_name = random_company()
        self.page.edit_company = random_company()
        self.page.edit_code = random_num(18)
        self.page.edit_hangye = random_job()
        self.page.edit_starttime = time.strftime("%Y-%m-%d")
        self.page.edit_endtime = time.strftime("%Y-%m-%d")
        self.page.edit_hangye.click()
        self.page.edit_num = random_num(3)
        self.page.edit_descipt = random_sentence()
        self.page.edit_person = random_name()
        phone1 = random_phone_number()
        phone.append(phone1)
        print(phone)
        self.page.edit_phone = phone1
        self.page.edit_save.click()
        time.sleep(2)

        self.page.search_phone = phone[0]
        self.page.search.click()
        time.sleep(2)

        # phone2 = self.driver.find_element_by_xpath(self.page.phone)

        self.assertNotEqual(phone,phone1)

    def test_4_删除(self):
        """
        机构管理-删除
        :return:
        """
        self.page.search_phone = phone[1]
        self.page.search.click()
        time.sleep(2)

        self.page.delete.click()
        time.sleep(2)

        self.page.delete_confirm.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

