# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.homePage import HomePage
import time
import unittest
from page.homePage import *
from page.loginPage import LoginPage
from run import *

class TestHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = HomePage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)
        #登陆
        self.login .input_name = username
        self.login .input_pw = password
        self.login .login_btn.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_createrecord(self):
        """
        首页-新建档案
        :return:
        """
        #新建档案

        self.page.create_record.click()
        time.sleep(2)

        self.page.input_name = self.page.name

        time.sleep(2)

        self.page.input_brithday = self.page.brithday

        time.sleep(2)

        self.page.input_phone = self.page.phone

        time.sleep(2)
        #提交
        self.page.commit.click()

        time.sleep(2)

        #开始测评
        self.page.start_test.click()

        time.sleep(2)
        #断言
        self.assertIsNotNone(self.page.context_assert)

    def test_startevaluation(self):
        """
        首页-开始测评
        :return:
        """
        #点击开始测评
        self.page.start_assess.click()
        time.sleep(2)
        #选择测评
        self.page.select_evaluetion.click()
        time.sleep(2)
        #选择档案
        self.page.select_record.click()
        time.sleep(2)
        #断言
        self.assertIsNotNone(self.page.evaluetion_assert)

if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    suite = unittest.TestSuite()
    suite.addTest(TestHome("test_login"))
    path = "../report/" + now + "result.html"
    fp = open(path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试首页功能")
    runner.run(suite)
    fp.close()
    unittest.main()

