# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.homePage import HomePage
import time
import unittest
from page.homePage import *
from page.loginPage import LoginPage
from page.assessPage import AssessPage
from run import *

class TestAssess(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = AssessPage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)

        #登陆
        self.login .input_name = username
        self.login .input_pw = password
        self.login .login_btn.click()
        time.sleep(2)

        # 切换到测评
        self.page.assess_btn.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_createassess_selectrecord(self):
        """
        测评-新建测评-选择档案-开始测评
        :return:
        """

        # 新建测评
        self.page.new_createassess.click()
        time.sleep(2)

        # 选择测评量表
        self.page.select_assess.click()
        time.sleep(2)

        # 选择档案
        self.page.select_assessrecord.click()
        time.sleep(2)

        # 断言
        self.assertIsNotNone(self.page.new_createassess_assert,msg='新建测评失败')


    def test_createassess_createrecord(self):
        """
        测评-新建测评-新建档案-开始测评
        :return:
        """
        # 新建测评
        self.page.new_createassess.click()
        time.sleep(2)

        # 选择测评量表
        self.page.select_assess.click()
        time.sleep(2)

        # 新建档案
        self.page.assess_createrecord.click()
        time.sleep(2)

        self.page.assess_recordname = self.page.name        # 姓名
        self.page.assess_recordbrith = self.page.brithday   # 出生日期
        self.page.assess_recordphone = self.page.phone      # 电话
        self.page.assess_recordcommit.click()               # 提交
        time.sleep(2)

        # 断言
        self.assertIsNotNone(self.page.new_createassess_assert,msg='新建测评失败')


    def test_lookassess(self):
        """
        测评-查看测评
        :return:
        """

        name1 = self.driver.find_element_by_xpath(self.page.name1).text
        # 查看测评
        self.page.look_assess.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.name3).text

        # 断言
        self.assertEqual(name1,name2,msg='查看测评失败')


    def test_printassess(self):
        """
        测评-打印测评
        :return:
        """

        name1 = self.driver.find_element_by_xpath(self.page.name1).text
        # 打印测评
        self.page.print_assess.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.name3).text

        # 断言
        self.assertEqual(name1,name2,msg='查看测评失败')


    # def test_delassess(self):
    #     """
    #     测评-删除测评
    #     :return:
    #     """
    #
    #     name1 = self.driver.find_element_by_xpath(self.page.name1).text
    #     # 删除测评
    #     self.page.del_assess.click()
    #     time.sleep(2)
    #
    #     # 确认删除
    #     self.page.del_confirm.click()
    #     time.sleep(2)
    #
    #     name2 = self.driver.find_element_by_xpath(self.page.name2).text
    #
    #     # 断言
    #     self.assertNotEqual(name1,name2,msg='查看测评失败')


    def test_searchassess(self):
        """
        测评-查询测评
        :return:
        """
        # 展开条件查询
        self.page.search_filter.click()
        time.sleep(2)

        # 获取测评ID
        assessID1 = self.driver.find_element_by_xpath(self.page.get_assessID).text

        # 根据id查询
        self.page.search_assessID = assessID1

        # 点击查询
        self.page.search_commit.click()
        time.sleep(2)

        assessID2 = self.driver.find_element_by_xpath(self.page.get_assessID).text
        # 断言
        self.assertEqual(assessID1,assessID1,msg='测评查询失败')


if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    suite = unittest.TestSuite()
    suite.addTest(TestAssess("test_assess"))
    path = "../report/" + now + "result.html"
    fp = open(path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试测评页面相关功能")
    runner.run(suite)
    fp.close()
    unittest.main()

