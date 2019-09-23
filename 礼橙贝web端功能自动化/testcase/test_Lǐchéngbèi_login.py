# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.loginPage import LoginPage
import time
import unittest
from page.loginPage import *
from run import *

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = LoginPage(self.driver)
        self.page.get(self.url)

    def tearDown(self):
        self.driver.close()


    def test_login(self):

        self.page.input_name = username
        self.page.input_pw = password
        self.page.login_btn.click()
        time.sleep(2)

        #断言
        self.assertEqual(self.page.content_assert,self.driver.current_url,msg='登陆失败')



if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    path = "../report/" + now + "result.html"
    fp = open(path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试登陆功能")
    runner.run(suite)
    fp.close()
    unittest.main()

