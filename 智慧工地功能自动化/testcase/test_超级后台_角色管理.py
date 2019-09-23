# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.rolePage import *
from page.loginPage import *
from run import *
from selenium.webdriver.common.action_chains import ActionChains
from generator import *

class TestRole(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = RolePage.url
        self.driver.maximize_window()
        self.page = RolePage(self.driver)
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

        self.page.role.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_1_新增角色(self):
        """
        角色管理-新增
        :return:
        """

        self.page.add_role.click()
        time.sleep(2)

        name = random_job()

        self.page.role_name = name

        self.page.all_quanxian.click()
        time.sleep(2)

        self.page.save_role.click()
        time.sleep(2)

        name1 = self.driver.find_element_by_xpath(self.page.save_name).text

        self.assertEqual(name,name1)

    def test_2_角色详情(self):
        """
        角色管理-详情
        :return:
        """

        self.page.role_detail.click()
        time.sleep(2)

    def test_3_角色编辑(self):
        """
        角色管理-编辑
        :return:
        """

        name1 = self.driver.find_element_by_xpath(self.page.save_name).text

        self.page.edit_role.click()
        time.sleep(2)

        self.page.edit_role_name = random_job()

        self.page.edit_save.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.save_name).text

        self.assertNotEqual(name1,name2)


    def test_4_角色删除(self):
        """
        角色管理-删除
        :return:
        """
        name1 = self.driver.find_element_by_xpath(self.page.save_name).text

        self.page.del_role.click()
        time.sleep(2)

        self.page.del_confirm.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.save_name).text

        self.assertNotEqual(name1,name2)


if __name__ == '__main__':
    unittest.main()

