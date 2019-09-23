# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.projectloginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
import os
from page.Page_综合管理_项目管理 import *
path = r'G:\自动化测试脚本\工地卫士机构后台功能自动化\testcase\jiaobe.exe'
phone = []
phone.append(random_phone_number())

class TestProjectLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = ProjectmanagePage.url
        self.driver.maximize_window()
        self.page = ProjectmanagePage(self.driver)
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
        self.page.project_management.click()
        time.sleep(2)

        #*****************************切换到账号管理*****************************结束


    def tearDown(self):
        self.driver.close()



    def test_1_项目编辑(self):
        """
        系统管理-项目部信息-编辑
        :return:
        """

        self.page.edit.click()
        time.sleep(2)

        self.page.edit_projectname = random_company()
        self.page.edit_engineeringname = random_company()
        self.page.premit_code = random_num(18)
        self.page.edit_company = random_company()
        self.page.edit_companycode = random_num(18)
        self.page.edit_projectstatus.click()
        time.sleep(2)
        self.page.statu1.click()
        time.sleep(1)
        self.page.edit_projectaddress.click()
        time.sleep(1)

        self.page.adr1.click()
        self.page.adr2.click()
        self.page.adr3.click()
        self.page.adr4.click()


        self.page.project_type.click()
        time.sleep(2)
        self.page.type1.click()
        time.sleep(1)

        self.page.organizePurposeType.click()
        time.sleep(2)
        self.page.PurposeType.click()
        time.sleep(2)

        self.page.buildingArea = random_num(4)
        self.page.responsorName = random_name()
        self.page.responsorPhone = random_phone_number()
        self.page.starttime = time.strftime("%Y-%m-%d")
        self.page.endtimt = '2030-12-30'
        self.page.upload_pingmian.click()
        time.sleep(5)

        os.system(path)
        time.sleep(5)

        self.page.place.click()
        time.sleep(2)

        self.page.inputaddress = '杭州市西湖区中天.-MCCB座'
        self.page.click_search.click()
        time.sleep(1)
        self.page.address_confirm.click()
        time.sleep(2)

        self.page.mAPPID = random_num(8)
        self.page.APPKEY = random_num(8)

        self.page.edit_save.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()

