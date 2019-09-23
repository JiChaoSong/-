# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from page.loginPage import LoginPage
import time
import unittest
from page.loginPage import *
from page.loginPage import LoginPage
from page.personalcentePage import PersonalCenterPage
from PIL import Image, ImageEnhance
from Processingcodes import *
from selenium.webdriver.firefox.options import Options
from run import *



class TestPersonalCenter(unittest.TestCase):
    def setUp(self):
        self.firefox_options = Options()
        self.firefox_options.add_argument('--headless')
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = PersonalCenterPage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)



        #登陆
        self.login .input_name = username
        self.login .input_pw = password
        self.login .login_btn.click()
        time.sleep(2)

        # 鼠标悬停头像上
        move = self.driver.find_element_by_xpath(self.page.center)
        ActionChains(self.driver).move_to_element(move).perform()
        time.sleep(2)
        # 点击个人中心
        self.page.personalcenter.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    # def test_personalinfo(self):
    #     """
    #     个人中心-个人信息
    #     :return:
    #     """
    #     # 账号信息
    #     info = self.driver.find_element_by_xpath(self.page.accountinfo).text
    #
    #     # 断言
    #     self.assertEqual(info,self.username,msg='信息错误')


    def test_editpassword(self):
        """
        个人中心-修改密码
        :return:
        """

        # 点击修改密码
        self.page.edit_password.click()
        time.sleep(2)
        """
        批量获取验证码
        """
        # while True:
        #     #截图
        #     self.driver.get_screenshot_as_file("./code.png")
        #     time.sleep(1)
        #     crop()
        #     #点击下一张，
        #     self.page.next_code.click()
        #     time.sleep(1)



if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    # now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # suite = unittest.TestSuite()
    # suite.addTest(TestPersonalCenter("test_login"))
    # path = "../report/" + now + "result.html"
    # fp = open(path, 'wb')
    # runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试登陆功能")
    # runner.run(suite)
    # fp.close()

    unittest.main()

