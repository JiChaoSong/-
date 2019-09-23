#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------
    Author:     JiChao_Song
--------------------------------------
"""
__author__ = 'JiChao_Song'

import unittest



def get_test_cases(dirpath):
    # dirpath是存放测试用例的文件路径
    test_cases = unittest.TestSuite()
    # 测试用例均使用"test_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_Lǐchéngbèi_personalcenter.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':

    for i in range(20):
        get_test_cases('../testcase')
        print(i)
        i +=1
