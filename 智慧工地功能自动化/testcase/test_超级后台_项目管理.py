# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page import loginPage
import time
import unittest
from page.projectPage import *
from page.loginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
import os
from generator import *

path = r'G:\自动化测试脚本\智慧工地功能自动化\testcase\jiaobe.exe'
name = []
name.append(random_company())



class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = ProjectPage.url
        self.driver.maximize_window()
        self.page = ProjectPage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)
        self.username = username['iotrack']
        self.password = password['iotrack']
        #*****************************登录*****************************开始

        self.login.username = self.username
        self.login.password = self.password

        self.login.login.click()
        time.sleep(2)

        #*****************************登录*****************************结束

        #*****************************切换到项目*****************************开始

        self.page.project.click()
        time.sleep(2)

        #*****************************切换到项目*****************************结束

    def tearDown(self):
        self.driver.close()

    def test_1_新增项目(self):
        """
        项目管理-新增项目
        :return:
        """
        self.page.project_add.click()
        time.sleep(2)

        self.page.project_name = name[0]

        self.page.project_organize.click()
        time.sleep(2)

        self.page.organize1.click()
        time.sleep(2)

        self.page.project_deparment.click()
        time.sleep(2)

        self.page.department1.click()
        time.sleep(2)

        self.page.project_save.click()
        time.sleep(2)


    def test_2_项目编辑(self):
        """
        项目管理-编辑项目
        :return:
        """

        self.page.search_projectname = name[0]
        self.page.search.click()
        time.sleep(2)


        self.page.edit.click()
        time.sleep(2)
        name1 = random_company()
        name.append(name1)
        self.page.edit_name = name[1]
        self.page.edit_save.click()
        time.sleep(2)


    # def test_3_项目删除(self):
    #     """
    #     项目管理-删除
    #     :return:
    #     """
    #
    #     # self.page.search_projectname = name[1]
    #     self.page.search_projectname = '万迅电脑网络有限公司'
    #     time.sleep(3)
    #
    #
    #     self.page.delete.click()
    #     time.sleep(2)
    #     self.page.delete_confirm.click(2)
    #     time.sleep(2)



if __name__ == '__main__':
    unittest.main()

