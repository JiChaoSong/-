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

class AssessPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.home_url
    url = home_url + '/'


    #*****************************测评-新建测评*****************************开始

    # 测评按钮
    assess_btn = PageElement(xpath = '/html/body/div/div/div[1]/div[1]/div/ul/li[3]/a')

    # 新建测评按钮
    new_createassess = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[2]/button')

    # 选择测评
    select_assess = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[5]/div[1]/'
                                        'div/div[2]/div/div[1]')

    # 选择测评档案(默认选择第一个）
    select_assessrecord = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[5]/'
                                              'div[2]/div/div[2]/div/div[4]/div/div[1]/div[3]/'
                                              'table/tbody/tr[1]/td[1]/div/span')

    # 选择新建测评档案
    assess_createrecord = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[5]/'
                                              'div[2]/div/div[2]/div/div[3]/button[3]')
    # 新建档案-姓名
    assess_recordname = PageElement(xpath='/html/body/div[1]/div/div[2]/section/div/div[5]/' \
                                           'div[3]/div/div/div[2]/div/form/div[1]/div[1]/div[2]/' \
                                           'div/div[1]/div/div/input')

    # 新建档案-出生日期
    assess_recordbrith = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[5]/'
                                            'div[3]/div/div/div[2]/div/form/div[1]/div[1]/div[2]/'
                                            'div/div[3]/div/div/input')

    # 新建档案-手机号
    assess_recordphone = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[5]/'
                                             'div[3]/div/div/div[2]/div/form/div[1]/div[2]/div[2]/'
                                             'div/div[1]/div/div/input')

    # 新建档案-提交
    assess_recordcommit = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[5]/'
                                              'div[3]/div/div/div[3]/div/button[2]')


    # 开始测评页断言
    new_createassess_assert = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[1]')

    #*****************************测评-新建测评*****************************结束


    #*****************************查看测评结果*****************************开始

    # 查看测评-按钮
    look_assess = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[4]/div/div[1]/'
                                      'div[3]/table/tbody/tr[1]/td[1]/div/span[1]')

    look_assert = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[6]/div/div/'
                                      'div[2]/div/div[2]/div[2]')

    #*****************************查看测评结果*****************************结束

    #*****************************打印测评结果*****************************开始

    # 打印测评结果
    print_assess = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[4]/div/div[1]/'
                                       'div[3]/table/tbody/tr[1]/td[1]/div/span[2]')

    # 点击打印
    print_assess_result = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[6]/'
                                              'div/div/div[2]/div/div[1]/button')

    # 断言
    print_assert = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[6]/div/div/'
                                       'div[2]/div/div[2]/div[2]')
    
    #*****************************打印测评结果*****************************结束

    #*****************************删除测评*****************************开始

    # 删除测评
    del_assess = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[4]/div/div[1]/div[3]/'
                                     'table/tbody/tr[1]/td[1]/div/span[3]')

    # 确认删除
    del_confirm = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')

    # 断言
    name1 = '/html/body/div[1]/div/div[2]/section/div/div[4]/div/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
    name2 = '/html/body/div[1]/div/div[2]/section/div/div[4]/div/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
    name3 = '/html/body/div[1]/div/div[2]/section/div/div[6]/div/div/div[2]/div/div[2]/table[1]/tbody/tr[1]' \
            '/td[1]/div/div[2]'
    name4 = '/html/body/div[1]/div/div[2]/section/div/div[6]/div/div/div[2]/div/div[2]/table[1]/tbody/tr[1]' \
            '/td[1]/div/div[2]'
    #*****************************删除测评*****************************结束


    #*****************************条件查询*****************************开始

    # 条件筛选
    search_filter  = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[3]/div/div[1]/div/i')

    # 根据测评ID查询
    search_assessID = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[3]/div/div[2]/'
                                          'div/div[1]/div[1]/div[1]/div[2]/div/input')

    # 获取测评ID
    get_assessID = '/html/body/div/div/div[2]/section/div/div[4]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'

    # 点击查询
    search_commit = PageElement(xpath = '/html/body/div/div/div[2]/section/div/div[3]/div/div[2]/div/div[2]/button[1]')



    #*****************************条件查询*****************************结束



    #*****************************数据*****************************开始

    name = random_name()
    phone = random_phone_number()
    brithday = age_month(random.randint(1,72))

    #*****************************数据*****************************结束