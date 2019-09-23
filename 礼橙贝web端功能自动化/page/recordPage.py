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

class RecordPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.home_url
    url = home_url+'/'

    #*****************************新建档案-元素*****************************开始

    # 点击菜单栏-档案
    record = PageElement(xpath = '//*[@id="app"]/div/div[1]/div[1]/div/ul/li[2]/a')

    # 新建档案
    create_record = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[2]/button[1]/span')

    # 姓名
    input_name = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[2]/div/div/'
                                     'div[2]/div/form/div[1]/div[1]/div[2]/div/div[1]/div/div/input')

    # 出生日期
    input_brithday = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[2]/div/'
                                         'div/div[2]/div/form/div[1]/div[1]/div[2]/div/div[3]/div/div/input')

    # 手机号
    input_phone = PageElement(xpath= '//*[@id="app"]/div/div[2]/section/div/div[4]/div[2]/div/div/div[2]/'
                                     'div/form/div[1]/div[2]/div[2]/div/div[1]/div/div/input')

    # 提交
    commit = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[2]/div/div/div[3]/div/'
                                 'button[2]/span')

    # 开始测评
    start_test = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[3]/div[1]/div/div[2]/'
                                     'div/div[1]')

    # 断言
    context_assert = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[1]')
    #*****************************新建档案-元素*****************************结束

    #*****************************打印空白档案-元素*****************************开始

    # 点击打印空白档案-按钮
    print_record = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[2]/button[2]/span')

    # 断言
    Personal_profile = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[4]/div/div/'
                                           'div[2]/div/div[2]/div[1]/div[2]')

    #*****************************打印空白档案-元素*****************************结束

    #*****************************查看档案-修改档案*****************************开始
    # 姓名断言
    name_assert = '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[2]/div[2]'

    # 查看档案(默认第一条)
    look_record = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/'
                                      'table/tbody/tr[1]/td[1]/div/span[1]')

    # 修改档案
    edit_record = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/button[3]/span')

    # 姓名修改
    edit_name = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[6]/div/div/div[2]/div/form/'
                                    'div[1]/div[1]/div[2]/div/div[1]/div/div/input')

    clear_name = '//*[@id="app"]/div/div[2]/section/div/div[6]/div/div/div[2]/div/form/div[1]/div[1]/' \
                 'div[2]/div/div[1]/div/div/input'
    # 手机号修改
    edit_phone = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[6]/div/div/div[2]/div/form/'
                                     'div[1]/div[2]/div[2]/div/div[1]/div/div/input')

    clear_phone = '//*[@id="app"]/div/div[2]/section/div/div[6]/div/div/div[2]/div/form/' \
                  'div[1]/div[2]/div[2]/div/div[1]/div/div/input'
    # 保存修改
    edit_save = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[6]/div/div/div[3]/div/button[2]')

    # 断言(第一条档案信息的姓名元素)
    edit_assert = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
    #*****************************查看档案-修改档案*****************************结束

    #*****************************查看档案-删除档案*****************************开始

    # 删除档案
    delete_record = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')

    # 要删除档案的姓名
    del_name = '/html/body/div[1]/div/div[2]/section/div/div[2]/div[1]/div[2]/div[2]'

    # 确认删除
    delete_confirm = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')

    # 删除之后的档案列表第一条的姓名
    record_name = '/html/body/div[1]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'

    #*****************************查看档案-删除档案*****************************结束

    #*****************************查看档案-新建测评*****************************开始

    # 新建测评
    create_assess = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/button[1]/span')

    # 选择测评
    select_assess1 = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[7]/div[1]/div/div[2]/div/div[1]')

    # 断言
    create_assess_assert = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[1]')

    #*****************************查看档案-新建测评*****************************结束

    """
    #*****************************查看档案-查看测评结果*****************************开始

    #*****************************查看档案-查看测评结果*****************************结束

    #*****************************查看档案-打印测评结果*****************************开始

    #*****************************查看档案-打印测评结果*****************************结束

    #*****************************查看档案-删除测评结果*****************************开始

    #*****************************查看档案-删除测评结果*****************************结束
    """

    #*****************************开始测评*****************************开始

    # 开始测评
    start_assess = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/'
                                       'table/tbody/tr[1]/td[1]/div/span[2]')

    # 选择测评
    select_assess2 = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[3]/div[1]/div/'
                                         'div[2]/div/div[1]')

    # 断言
    start_assess_assert = PageElement(xpath = '//*[@id="app"]/div/div[2]/section/div/div[1]')

    #*****************************开始测评*****************************结束


    #*****************************条件查询*****************************开始

    # 展开查询条件
    open_up = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[1]/div/i')

    # 根据姓名查询
    search_name = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/div[1]/div[2]/'
                                      'div[1]/div[2]/div/input')

    # 根据手机号查询
    search_phone = PageElement(xpath = '//*[@id="el-collapse-content-1645"]/div/div[1]/div[3]/div[2]/div[2]/div/input')

    # 根据月龄查询
    search_age = PageElement(xpath = '//*[@id="el-collapse-content-1645"]/div/div[1]/div[4]/div/div[2]/div/input')

    # 获取姓名
    get_anme = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'

    # 查询结果
    result_name = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/div'

    # 点击查询
    search_btn = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/div[3]/button[1]')

    #*****************************条件查询*****************************结束


    #*****************************翻页相关元素*****************************开始

    # 第二页
    next_page = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div[4]/div[1]/div[2]/div/ul/li[2]')

    # 翻页之前的姓名
    font_name = '/html/body/div[1]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
    # 翻页之后的姓名
    next_name = '/html/body/div[1]/div/div[2]/section/div/div[4]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'

    #*****************************翻页相关元素*****************************结束


    #*****************************数据*****************************开始

    name = random_name()
    phone = random_phone_number()
    brithday = age_month(random.randint(1,72))

    #*****************************数据*****************************结束