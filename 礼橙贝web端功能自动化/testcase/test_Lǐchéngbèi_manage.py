# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.homePage import HomePage
import time
import unittest
from page.homePage import *
from page.loginPage import LoginPage
from page.managementPage import ManagementPage
from run import *


class TestManage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = ManagementPage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)

        #登陆
        self.login .input_name = username
        self.login .input_pw = password
        self.login .login_btn.click()
        time.sleep(2)

        # 切换到管理
        self.page.manage_btn.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_createacconut(self):
        """
        管理-账号管理-新建账号
        :return:
        """
        # 点击新建账号
        self.page.account_number_create.click()
        time.sleep(2)

        account = self.page.account_num
        # 输入姓名
        self.page.account_name = self.page.name
        # 输入账号
        self.page.account_number = account
        # 输入手机号
        self.page.account_phone = self.page.phone
        # 点击提交
        self.page.account_commit.click()
        time.sleep(2)

        account_text = self.driver.find_element_by_xpath(self.page.account).text
        # 断言
        self.assertEqual(account,account_text)


    def test_editaccount(self):
        """
        管理-账号管理-修改账号（默认修改第一条）
        :return:
        """

        # 获取修改之前的账号姓名
        name1 = self.driver.find_element_by_xpath(self.page.accname).text

        # 点击修改账号
        self.page.edit_account.click()
        time.sleep(2)


        # 修改姓名
        self.page.edit_account_name = self.page.name

        # 点击保存修改
        self.page.edit_account_confire.click()
        time.sleep(2)

        # 获取修改之后的账号姓名
        name2 = self.driver.find_element_by_xpath(self.page.accname).text

        # 断言
        self.assertNotEqual(name1,name2)


    def test_resetpw(self):
        """
        管理-账号管理-修改-重置密码
        :return:
        """
        # 点击修改账号
        self.page.edit_account.click()
        time.sleep(2)

        # 点击重置密码
        self.page.reset_password.click()
        time.sleep(2)

        # 确认重置
        self.page.reset_confire.click()
        time.sleep(2)

        # 获取当前url
        url = self.driver.current_url

        # 断言
        self.assertEqual(url,self.page.urls)


    def test_delaccount(self):
        """
        管理-账号中心-修改-删除账号
        :return:
        """
        # 获取删除之前的账号姓名
        name1 = self.driver.find_element_by_xpath(self.page.accname).text

        # 点击修改账号
        self.page.edit_account.click()
        time.sleep(2)

        # 点击删除账号
        self.page.del_account.click()
        time.sleep(2)

        # 点击确认删除
        self.page.del_confire.click()
        time.sleep(2)

        # 获取删除之后的账号姓名
        name2 = self.driver.find_element_by_xpath(self.page.accname).text

        # 断言
        self.assertNotEqual(name1,name2)

if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    suite = unittest.TestSuite()
    suite.addTest(TestManage("test_manage"))
    path = "../report/" + now + "result.html"
    fp = open(path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试首页功能")
    runner.run(suite)
    fp.close()
    unittest.main()

