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

class LoginPage(PageObject):

    # 当前测试页面的测试网址url
    login_url = Url.login_url
    url = login_url+'/'

    # 查询元素
    input_name = PageElement(xpath="/html/body/div/div/form/div[2]/div/div/input")          #输入用户名
    input_pw = PageElement(xpath = '/html/body/div/div/form/div[3]/div/div[1]/input')       #输入密码
    remeber_me = PageElement(xpath = '/html/body/div/div/form/div[4]/label[1]/span[2]')     #记住密码
    auto_login = PageElement(xpath = '/html/body/div/div/form/div[4]/label[2]/span[2]')     #自动登陆
    forget_pw = PageElement(xpath = '/html/body/div/div/form/div[4]/span')                  #忘记密码
    login_btn = PageElement(xpath='/html/body/div/div/form/button')                         #登陆按钮
    wel_info = PageElement(xpath = '/html/body/div/div/div[1]/div[1]/div/span/span')        #登陆成功欢迎字段

    # 查询内容
    # search_content = "hello"

    # 断言
    content_assert = Url.home_url


    #用户数据
    username = 'zhihan123456'
    password = username[-6:]
