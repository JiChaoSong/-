#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------
    Author:     JiChao_Song
--------------------------------------
"""
__author__ = 'JiChao_Song'
import random
import os
import time
from selenium import webdriver
# 两种方法任选其一，都是指向同一个文件
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

pa_list = []
path = '../testcase/'
list = []

for root,dirs,files in os.walk(path):
    pa_list.append(root)
list.append(pa_list[2])
list.append(pa_list[4])
list.append(pa_list[6])
# print(random.randint(0, 6))
print(pa_list)
print(pa_list[2])
print(pa_list[4])
print(pa_list[6])
print(pa_list[2:5])
print(list)
# driver = webdriver.Firefox()
# driver.get('http://localhost:63342/%E6%99%BA%E6%85%A7%E5%B7%A5%E5%9C%B0%E5%8A%9F%E8%83%BD%E8%87%AA%E5%8A%A8%E5%8C%96/test.html')
# print(driver.title)
# # 定位到下拉选择框
# # selector = driver.find_element_by_id("selectdemo")
# selector = driver.find_element_by_xpath('//*[@id="selectdemo"]')
# time.sleep(5)
# # 选择"篮球运动员"
# selector.find_element_by_xpath("/html/body/select/option[3]").click()
# # selector.find_elements_by_tag_name("option")[2].click()

#
# a = '18088880000'
#
# print(a[-8:])

