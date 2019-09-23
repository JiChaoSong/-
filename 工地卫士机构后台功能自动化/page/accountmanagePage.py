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
from .generator import *
from .month_age import *

class AccountManagePage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.organize_url
    url = home_url+'/'

    # 系统管理
    sysmanage = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[6]/div')

    # 账号管理
    accountmanage = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[6]/ul/a[1]/li')

    #*****************************新建账号*****************************开始

    # 点击新建
    account_add = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[1]/button[2]')

    # 账号姓名
    account_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/'
                                       'div/div/div[4]/div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')

    # 账号手机号
    account_phone = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                        'div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/input')

    # 岗位选择
    account_job = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                      'div[2]/form/div[4]/div/div[2]/div/div/div[1]/div/div[2]/input')

    # 岗位1
    job1 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
    job2 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[2]')
    job3 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[3]')
    job4 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[4]')
    job5 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[5]')
    job6 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[6]')
    job7 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[7]')
    job8 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[8]')

    # 保存
    account_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/'
                                       'div/div/div/div[4]/div/div[3]/div/button[2]')
    #*****************************新建账号*****************************结束

    #*****************************项目权限*****************************开始

    # 点击项目权限
    projectset = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/'
                                     'div/div/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/span[1]')

    # 全选
    all_select = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                     'div[2]/form/div/div/div[2]/div/div/div[1]/div/label/span[1]/span')

    # 保存
    projectset_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                          'div/div[3]/div/button[2]')
    
    #*****************************项目权限*****************************结束
    
    #*****************************搜索*****************************开始

    # 搜索
    search = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[2]/button[2]')

    # 手机号搜索
    search_phone = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                       'div[1]/div[4]/div/input')

    #*****************************搜索*****************************结束

    #*****************************详情*****************************开始

    # 点击详情
    detail = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/'
                                 'div/div[1]/div[3]/table/tbody/tr/td[5]/div/span[2]')
    name = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/div/div[1]/div[3]/table/' \
           'tbody/tr/td[1]/div'

    phone = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/div/div[1]/div[3]/table/' \
            'tbody/tr/td[3]/div'
    detail_name = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/div[2]/form/div[1]/' \
            'div/div[2]/div/div/div[1]/span'
    detail_phone = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/div[2]/form/div[3]/' \
                   'div/div[2]/div/div/div[1]/span'

    detail_close = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                       'div/div[1]/button/i')
    
    #*****************************详情*****************************结束
    
    #*****************************编辑*****************************开始

    edit = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/div/div[1]/'
                               'div[3]/table/tbody/tr/td[5]/div/span[3]')

    edit_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                    'div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')

    edit_phone = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                     'div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/input')

    edit_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                    'div[3]/div/button[2]')
    #*****************************编辑*****************************结束
    
    
    #*****************************删除*****************************开始

    delete = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/div/'
                                 'div[1]/div[3]/table/tbody/tr/td[5]/div/span[4]')

    delete_confirm = PageElement(css = 'html body.el-popup-parent--hidden div.el-message-box__wrapper div.el-'
                                       'message-box div.el-message-box__btns button.el-button.el-button--de'
                                       'fault.el-button--small.el-button--primary')

    #*****************************删除*****************************结束