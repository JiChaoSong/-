# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.projectloginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
from page.accountmanagePage import *

phone = []
phone.append(random_phone_number())

class TestProjectLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = AccountManagePage.url
        self.driver.maximize_window()
        self.page = AccountManagePage(self.driver)
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

        self.page.sysmanage.click()
        time.sleep(2)
        self.page.accountmanage.click()
        time.sleep(2)

        #*****************************切换到账号管理*****************************结束


    def tearDown(self):
        self.driver.close()



    def test_1_新建账号(self):
        """
        系统管理-账号管理-新增账号
        :return:
        """

        self.page.account_add.click()
        time.sleep(2)

        self.page.account_name = random_name()
        self.page.account_phone = phone[0]
        self.page.account_job.click()
        time.sleep(2)
        self.page.job1.click()
        self.page.job2.click()
        self.page.job3.click()
        self.page.job4.click()
        time.sleep(2)
        # self.page.account_job.click()
        # time.sleep(2)
        self.page.account_save.click()
        time.sleep(2)


    def test_2_项目权限(self):
        """
        系统管理-账号管理-项目权限
        :return:
        """

        self.page.search_phone = phone[0]
        self.page.search.click()
        time.sleep(2)


        self.page.projectset.click()
        time.sleep(2)
        self.page.all_select.click()
        time.sleep(2)

        self.page.projectset_save.click()
        time.sleep(2)


    def test_3_详情(self):
        """
        系统管理-账号管理-详情
        :return:
        """

        self.page.search_phone = phone[0]
        self.page.search.click()
        time.sleep(2)

        phone1 = self.driver.find_element_by_xpath(self.page.phone).text
        self.page.detail.click()
        time.sleep(2)
        phone2 = self.driver.find_element_by_xpath(self.page.detail_phone).text

        self.page.detail_close.click()
        time.sleep(2)

        self.assertEqual(phone1,phone2)




    def test_4_编辑(self):
        """
        系统管理-账号管理-编辑
        :return:
        """

        self.page.search_phone = phone[0]
        self.page.search.click()
        time.sleep(2)


        self.page.edit.click()
        time.sleep(2)
        self.page.edit_name = random_name()
        phone1 = random_phone_number()
        phone.append(phone1)
        self.page.edit_phone = phone[1]

        self.page.edit_save.click()
        time.sleep(2)


    def test_5_删除(self):
        """
        系统管理-账号管理-删除
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

