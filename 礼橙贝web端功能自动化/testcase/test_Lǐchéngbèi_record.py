# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.homePage import HomePage
import time
import unittest
from page.homePage import *
from page.loginPage import LoginPage
from page.recordPage import RecordPage
from run import *


class TestRecord(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = LoginPage.url
        self.driver.maximize_window()
        self.page = RecordPage(self.driver)
        self.login = LoginPage(self.driver)
        self.page.get(self.url)


        #登陆
        self.login .input_name = username
        self.login .input_pw = password
        self.login .login_btn.click()
        time.sleep(2)
        # 档案
        self.page.record.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    def test_createrecord(self):
        """
        档案-新建档案
        :return:
        """
        #新建档案
        self.page.create_record.click()
        time.sleep(2)

        self.page.input_name = self.page.name
        self.page.input_brithday = self.page.brithday
        self.page.input_phone = self.page.phone
        self.page.commit.click()

        time.sleep(2)
        #选择测评
        self.page.start_test.click()

        time.sleep(2)
        #断言
        self.assertIsNotNone(self.page.context_assert)


    def test_printemptyrecord(self):
        """
        档案-打印空白档案
        :return:
        """
        #打印空白档案
        self.page.print_record.click()
        time.sleep(2)

        #断言
        self.assertIsNotNone(self.page.Personal_profile)


    def test_editrecord(self):
        """
        档案-修改档案
        :return:
        """
        # 点击查看档案（默认第一条）
        self.page.look_record.click()
        time.sleep(2)

        # 点击修改档案
        self.page.edit_record.click()
        time.sleep(2)

        name_list = []
        name_list.append(self.page.name)
        self.page.edit_name.clear()
        time.sleep(1)
        # self.driver.find_element_by_xpath(self.page.clear_name).clear()
        self.page.edit_name = name_list[-1]
        self.page.edit_phone.clear()
        time.sleep(1)
        # self.driver.find_element_by_xpath(self.page.clear_phone).clear()
        self.page.edit_phone = self.page.phone
        self.page.edit_save.click()
        time.sleep(2)

        name = self.driver.find_element_by_xpath(self.page.name_assert).text
        # 断言
        self.assertEqual(name_list[-1], name, msg='档案修改失败')


    def test_delrecord(self):
        """
        档案-删除档案
        :return:
        """

        # 点击查看档案（默认第一条）
        self.page.look_record.click()
        time.sleep(2)

        name1 = self.driver.find_element_by_xpath(self.page.del_name).text

        # 点击删除档案
        self.page.delete_record.click()
        time.sleep(2)

        # 确认删除
        self.page.delete_confirm.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.record_name).text

        # 断言
        self.assertNotEqual(name1,name2,msg='删除档案失败')


    def test_createassess(self):
        """
        档案-开始测评
        :return:
        """
        # 点击查看档案（默认第一条）
        self.page.look_record.click()
        time.sleep(2)

        # 查看档案-新建测评
        self.page.create_assess.click()
        time.sleep(2)

        # 选择测评
        self.page.select_assess1.click()
        time.sleep(2)

        # 断言
        self.assertIsNotNone(self.page.create_assess_assert)

    def test_startassess(self):
        """
        档案-开始测评
        :return:
        """

        # 点击开始测评
        self.page.start_assess.click()
        time.sleep(2)

        # 选择测评
        self.page.select_assess2.click()
        time.sleep(2)

        # 断言
        self.assertIsNotNone(self.page.start_assess_assert)



    def test_nextpage(self):
        """
        档案-翻页
        :return:
        """

        name1 = self.driver.find_element_by_xpath(self.page.font_name).text
        # 点击第二页
        self.page.next_page.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.next_name).text

        # 断言
        self.assertNotEqual(name1,name2,msg='翻页失败')


    def test_searchrecord(self):
        """
        档案-查询
        :return:
        """

        # 查询
        self.page.open_up.click()
        time.sleep(2)

        name1 = self.driver.find_element_by_xpath(self.page.get_anme).text

        self.page.search_name.click()
        time.sleep(2)

        self.page.search_name.send_keys(name1)

        self.page.search_btn.click()
        time.sleep(2)

        name2 = self.driver.find_element_by_xpath(self.page.record_name).text
        # 断言
        self.assertEqual(name1,name2,msg='查询失败')




if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    suite = unittest.TestSuite()
    suite.addTest(TestRecord("test_erecord"))
    path = "../report/" + now + "result.html"
    fp = open(path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试首页功能")
    runner.run(suite)
    fp.close()
    unittest.main()

