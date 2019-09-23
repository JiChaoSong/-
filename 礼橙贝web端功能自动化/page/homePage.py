#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------
    Author:     JiChao_Song
--------------------------------------
"""
__author__ = 'JiChao_Song'

from common.pageObject import PageObject, PageElement
from common.url import *
from .month_age import *
from .generator import *
import random



class HomePage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.home_url
    url = home_url+'/'

    # 查询元素
    create_record = PageElement(xpath='/html/body/div/div/div[2]/section/div/div/div[2]/ul/li[1]')       #新建档案
    start_assess = PageElement(xpath='/html/body/div/div/div[2]/section/div/div/div[2]/ul/li[2]')        #开始测评

    #*****************************新建档案*****************************开始
    # 姓名
    input_name = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div/div[5]/div/div/div[2]/div/'
                               'form/div[1]/div[1]/div[2]/div/div[1]/div/div/input')
    # 性别选择
    select_sale = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div/div[5]/div/div/div[2]/div/'
                                      'form/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/span/span/i')
    # 男
    male = PageElement(xpath = '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
    # 女
    female = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[2]')

    # 出生日期
    input_brithday = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div/div[5]/div/div/div[2]/'
                                         'div/form/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/input')
    # 手机号
    input_phone = PageElement(xpath ='//*[@id="app"]/div/div[2]/section/div/div/div[5]/div/div/div[2]/div/'
                                     'form/div[1]/div[2]/div[2]/div/div[1]/div/div/input')
    # 提交
    commit = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div/div[5]/div/div/div[3]/div/button[2]')

    # 开始测评
    start_test = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div/div[4]/div[1]/div/div[2]/div/div[1]')
    #*****************************新建档案*****************************结束

    #*****************************开始测评*****************************开始

    # 选择测评
    select_evaluetion = PageElement(
        xpath='//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[1]/div/div[2]/div/div[1]')

    # 选择档案(默认选择第一个)
    select_record = PageElement(xpath='//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[2]/div/div[2]/'
                                      'div/div[4]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/span')
    #*****************************开始测评*****************************结束




    #*****************************档案传入的data*****************************开始

    name = random_name()
    gender = random.choice(['男','女'])
    brithday = age_month(random.randint(1,72))          #age_month(月龄) 返回"%Y-%m-%d"
    phone = random_phone_number()

    #*****************************档案传入的data*****************************结束


    # 断言

    context_assert = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[1]')

    evaluetion_assert = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[1]')