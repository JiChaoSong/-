import unittest
import HTMLTestRunner
import time
from common.sendEmail import SendEmail




username = '180001'
password = '0001'


def get_test_cases(dirpath):
    # dirpath是存放测试用例的文件路径
    test_cases = unittest.TestSuite()
    # 测试用例均使用"test_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


if __name__ == '__main__':

    #*****************************设置登录账号和密码*****************************开始
    username = '180001'
    password = '0001'
    #*****************************设置登录账号和密码*****************************结束

    cases = get_test_cases('../testcase')
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
    test_reports_address = '../report'      # 测试报告存放位置
    filename = r'../report/' + now + 'report.html'  # 设置报告文件名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'礼橙贝web端主要功能自动化测试', description=u'详细测试结果如下:')
    runner.run(cases)
    fp.close()
    # 向指定邮箱发送测试报告的html文件
    time.sleep(6)
    # 查找最新生成的测试报告地址
    new_report_addr = SendEmail().acquire_report_address(test_reports_address)
    # 自动发送邮件
    SendEmail().send_email(new_report_addr)
