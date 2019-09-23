# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
from page.jobmanagePage import *
from selenium.webdriver.common.action_chains import ActionChains
from run import *
from page.projectloginPage import *

class TestProjectLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = JobManagePage.url
        self.driver.maximize_window()
        self.page = JobManagePage(self.driver)
        self.login = ProjectLoginPage(self.driver)
        self.page.get(self.url)
        self.username = username.get('project_department')
        self.password = password.get('project_department')

        #*****************************登录*****************************开始
        self.login.username.clear()
        self.login.username = self.username

        self.login.password = self.password

        self.login.login.click()
        time.sleep(2)
        #*****************************登录*****************************结束

        #*****************************切换到岗位管理*****************************开始

        self.page.sysmanage.click()
        time.sleep(2)
        self.page.jobmanage.click()
        time.sleep(2)

        #*****************************切换到岗位管理*****************************结束
    def tearDown(self):
        self.driver.close()


    def test_1_新增岗位(self):
        """
        系统管理-岗位管理-新增岗位
        :return:
        """
        self.page.job_add.click()
        time.sleep(2)

        self.page.job_name = random_job()
        self.page.job_pc.click()
        time.sleep(1)
        self.page.job_app.click()
        time.sleep(1)
        self.page.job_save.click()
        time.sleep(2)


    def test_2_岗位详情(self):
        """
        系统管理-岗位管理-详情
        :return:
        """

        jobname = self.driver.find_element_by_xpath(self.page.jobname).text
        self.page.detail.click()
        time.sleep(2)
        jobname1 = self.driver.find_element_by_xpath(self.page.detail_name).text

        self.assertEqual(jobname,jobname1)

    def test_3_编辑岗位(self):
        """
        系统管理-岗位管理-编辑
        :return:
        """

        self.page.edit.click()
        time.sleep(2)
        self.page.edit_name = random_job()
        self.page.edit_save.click()
        time.sleep(2)

    def test_4_删除岗位(self):
        """
        系统管理-岗位管理-删除
        :return:
        """

        self.page.delete.click()
        time.sleep(2)
        self.page.delete_confirm.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()

