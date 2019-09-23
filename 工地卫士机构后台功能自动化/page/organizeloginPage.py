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
    home_url = Url.organize_url
    url = home_url+'/'

    #*****************************登录*****************************开始

    # 账号
    username = PageElement(xpath = '/html/body/div[1]/div[1]/form/div[2]/div/div/input')

    # 密码
    password = PageElement(xpath = '/html/body/div[1]/div[1]/form/div[3]/div/div/input')

    # 点击登录

    login = PageElement(xpath = '/html/body/div[1]/div[1]/form/button')


    # 断言
    page_url = 'http://pre.iotrack.cn/organize/#/projectManage/project/index'
    #*****************************登录*****************************结束



    #*****************************登出*****************************开始

    # 头像
    image = '/html/body/div[1]/div[1]/div[1]/ul/div[2]/img'

    image2 = '/html/body/div[1]/div[1]/div[1]/ul/div[2]/img'


    # 点击退出
    quit = PageElement(xpath = '/html/body/div[1]/div[1]/div[1]/ul/div[2]/div/ul/li/span')

    quit2 = PageElement(xpath = '/html/body/div[1]/div[1]/div[1]/ul/div[2]/div/ul/li')
    #*****************************登出*****************************结束


    #*****************************个人信息*****************************开始

    # 点击个人信息
    info  = PageElement(xpath = '/html/body/div[1]/div[1]/div[1]/ul/div[2]/div/a/div/span')

    # 点击修改密码
    edit_password = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/'
                                        'div/div/div[4]/span/div/div[3]/button')

    # 旧密码
    old_password = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/'
                                       'div/div[5]/div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')

    # 新密码
    new_password = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                       'div[2]/form/div[2]/div/div[2]/div/div/div[1]/div/input')

    # 确认密码
    confirm_password = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                           'div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/input')

    # 点击保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/div[3]/'
                                    'div/button[2]')
    #*****************************个人信息*****************************结束