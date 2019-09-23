# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
import random
from page.managerPage import *
from page.loginPage import *
from run import *
from selenium.webdriver.common.action_chains import ActionChains
from page.generator import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from generator import *

class TestRole(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.url = ManagerPage.url
        self.driver.maximize_window()
        self.page = ManagerPage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)
        self.username = username['iotrack']
        self.password = password['iotrack']

        # 登录
        self.login.username.clear()
        self.login.username = self.username
        self.login.password = self.password

        self.login.login.click()
        time.sleep(2)

        self.page.manager.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_1_添加管理员(self):
        """
        管理员管理-新增
        :return:
        """

        self.page.add_manage.click()
        time.sleep(2)

        name = random_name()

        self.page.manager_name = name
        self.page.manager_phone = random_phone_number()

        self.page.manager_role.click()
        time.sleep(2)

        # selector = self.driver.find_elements_by_xpath('/html/body/div[4]')
        #
        # selector

        self.page.manager_role1.click()
        self.page.manager_role2.click()
        self.page.manager_role3.click()
        self.page.manager_role4.click()
        self.page.manager_role5.click()
        self.page.manager_role6.click()
        time.sleep(2)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                          'div[2]/form/div[3]/div/div[2]/div/div/div/div/div[1]').click()
        self.page.manager_remark = random_sentence()

        self.page.manager_save.click()
        time.sleep(2)


    def test_2_详情(self):
        """
        管理员管理-详情
        :return:
        """

        self.page.next_page.click()
        time.sleep(2)

        self.page.detail.click()
        time.sleep(2)

        self.page.detail_close.click()
        time.sleep(2)


    def test_3_编辑(self):
        """
        管理员管理-编辑
        :return:
        """

        self.page.next_page.click()
        time.sleep(2)

        self.page.edit.click()
        time.sleep(2)

        self.page.edit_name = random_name()
        self.page.edit_phone = random_phone_number()
        self.page.edit_remark = random_sentence()
        self.page.edit_save.click()
        time.sleep(2)



    def test_4_删除(self):
        """
        管理员管理-删除
        :return:
        """

        name1 = self.driver.find_element_by_xpath(self.page.name2).text

        self.page.next_page.click()
        time.sleep(2)

        self.page.delete.click()
        time.sleep(2)

        self.page.delete_confirm.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.name2).text


        self.assertNotEqual(name1,name2)


if __name__ == '__main__':
    unittest.main()

