# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.organizePage import *
from page.organizeloginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
from page.generator import *


organize_name = []
organize_name.append(random_company())

class TestOrganize(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = OrganizePage.url
        self.driver.maximize_window()
        self.page = OrganizePage(self.driver)
        self.page.get(self.url)
        self.username = username.get('organize')
        self.password = password.get('organize')
        self.login = LoginPage(self.driver)

        self.login.username.clear()
        self.login.username = self.username

        self.login.password = self.password

        self.login.login.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    def test_1_新增项目部(self):
        """
        机构管理员-项目部管理-新增项目部
        :return:
        """

        self.page.add_organize.click()
        time.sleep(2)

        self.page.add_organize_name = organize_name[0]
        self.page.add_organize_zb = random_company()
        self.page.add_organize_code =random_num(18)
        self.page.add_organize_bank = random_address()
        self.page.add_organize_banknum = random_num(15)
        self.page.add_organize_person = random_name()
        self.page.add_organize_phone = random_phone_number()
        # self.page.add_organize_phone = '15927549205'

        self.page.add_save.click()
        time.sleep(2)


    def test_2_详情(self):
        """
        机构管理员-项目部管理-详情
        :return:
        """
        self.page.search_name = organize_name[0]
        self.page.search.click()
        time.sleep(2)

        name1 = self.driver.find_element_by_xpath(self.page.name1).text

        self.page.detail.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.detail_name).text

        self.assertEqual(name1,name2)

    def test_3_编辑(self):
        """
        机构管理员-项目部管理-编辑
        :return:
        """
        self.page.search_name = organize_name[0]
        self.page.search.click()
        time.sleep(2)

        name1 = self.driver.find_element_by_xpath(self.page.name1).text

        self.page.edit.click()
        time.sleep(2)
        organizename = random_company()
        organize_name.append(organizename)
        self.page.add_organize_name = organize_name[1]
        self.page.add_organize_zb = random_company()
        self.page.add_organize_code =random_num(18)
        self.page.add_organize_bank = random_address()
        self.page.add_organize_banknum = random_num(15)
        self.page.add_organize_person = random_name()
        # self.page.add_organize_phone = random_phone_number()

        self.page.edit_save.click()
        time.sleep(2)



        self.assertNotEqual(name1,organize_name[1])


    def test_4_删除(self):
        """
        机构管理员-项目部管理-删除
        :return:
        """

        self.page.search_name = organize_name[1]
        self.page.search.click()
        time.sleep(2)

        name1 = self.driver.find_element_by_xpath(self.page.name1).text

        self.page.delete.click()
        time.sleep(2)

        self.page.delete_confirm.click()
        time.sleep(2)

        # name2 = self.driver.find_element_by_xpath(self.page.name).text
        #
        # self.assertNotEqual(name1,name2)


if __name__ == '__main__':
    unittest.main()

