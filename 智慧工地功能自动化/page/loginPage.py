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

class LoginPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.iotrack_url
    url = home_url+'/'

    #*****************************登录*****************************开始

    # 账号
    username = PageElement(xpath = '/html/body/div/div/form/div[2]/div/div/input')

    # 密码
    password = PageElement(xpath = '/html/body/div/div/form/div[3]/div/div/input')

    # 点击登录

    login = PageElement(xpath = '/html/body/div/div/form/button')


    # 断言
    page_url = 'http://pre.iotrack.cn/admin/#/organizeManage/organize/index'
    #*****************************登录*****************************结束



    #*****************************登出*****************************开始

    # 头像
    image = '/html/body/div/div/div[1]/ul/div/img'

    # 点击退出
    quit = PageElement(xpath = '/html/body/div/div/div[1]/ul/div/div/ul/li')

    #*****************************登出*****************************结束