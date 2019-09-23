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

class ManagementPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.home_url
    url = home_url + '/'


    #*****************************管理中心*****************************开始

    # 管理
    manage_btn = PageElement(xpath = '/html/body/div/div/div[1]/div[1]/div/ul/li[4]/a')

    #*****************************账号管理*****************************开始

    # 新建账号
    account_number_create = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div/div[2]/button')

    # 新建账号-姓名
    account_name = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[1]/div[1]/'
                                       'form/div[1]/div/div/input')

    # 新建账号-账号
    account_number = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[1]/div[1]/'
                                         'form/div[2]/div/div/input')

    # 新建账号-手机号
    account_phone = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[1]/div[1]/'
                                        'form/div[3]/div/div/input')

    # 新建账号-提交
    account_commit = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[2]/div/button')

    # 错误提示
    tip8 = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[1]/div[1]/form/div[2]/div/div[2]'
    tip24 = '/html/body/div[2]/p'


    # 新增成功断言 判断账号是否一致
    account = '/html/body/div/div/div[2]/section/div/section/div/div/div[3]/div/div[1]/div[3]/table/' \
              'tbody/tr[1]/td[3]/div'

    accname = '/html/body/div/div/div[2]/section/div/section/div/div/div[3]/div/div[1]/div[3]/table/' \
              'tbody/tr[1]/td[2]/div'
    # 点击修改 默认选择第一个
    edit_account = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div/div[3]/div/'
                                       'div[1]/div[3]/table/tbody/tr[1]/td[1]/div')

    # 姓名修改
    edit_account_name = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[1]/'
                                            'div[1]/form/div[1]/div/div/input')

    # 点击确认修改
    edit_account_confire = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/'
                                               'div[2]/div/button[1]')

    # 重置密码
    reset_password = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[2]/'
                                      'div/button[2]')
    # 确认重置
    reset_confire = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')

    # 重置成功后的URL
    urls = 'http://test.childfit.cn/admin/#/manage/all/account/list'

    # 删除账号
    del_account = PageElement(xpath = '/html/body/div/div/div[2]/section/div/section/div/div[2]/div[2]/'
                                      'div/button[3]')

    # 确认删除
    del_confire = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')



    #*****************************账号管理*****************************结束

    #*****************************管理中心*****************************结束

    #*****************************数据*****************************开始
    # 姓名
    name = random_name()
    # 账号
    account_num = random_password()
    # 手机号
    phone = random_phone_number()
    #*****************************数据*****************************结束