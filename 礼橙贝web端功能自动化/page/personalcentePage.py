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

class PersonalCenterPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.home_url
    url = home_url+'/'

    #*****************************个人中心-个人信息*****************************开始

    # 个人中心-鼠标悬停
    center = '/html/body/div/div/div[1]/div[1]/div/div/img'

    # 个人中心
    personalcenter = PageElement(xpath = '/html/body/div/div/div[1]/div[1]/div/div/div/ul/li[1]')

    # 获取账号信息
    accountinfo = '/html/body/div/div/div[2]/section/div/section/div/div/div[2]/div[2]'

    #*****************************个人中心-个人信息*****************************结束
    
    #*****************************个人中心-修改密码*****************************开始

    # 点击修改密码
    edit_password = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/div/ul/li/div[3]/a')


    # 获取验证码为值
    code = '/html/body/div[1]/div/div[2]/section/div/div/ul/li/div[3]/a'

    # 下一张
    next_code = PageElement(xpath = '/html/body/div[1]/div/div[2]/section/div/section/div/div/form/'
                                    'div[4]/div/div[2]/div/div/div/span')

    #*****************************个人中心-修改密码*****************************结束