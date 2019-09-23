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

class ManagerPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.iotrack_url
    url = home_url+'/'

    manager = PageElement(xpath = '/html/body/div[1]/div/div[2]/ul/div/a[5]/li')

    name = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]'

    #*****************************添加管理员*****************************开始

    # 添加管理员
    add_manage  = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/button')

    # 姓名
    manager_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                       'div/div[2]/form/div[1]/div/div[2]/div/div/div/div/input')

    # 手机号
    manager_phone = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                        'div/div[2]/form/div[2]/div/div[2]/div/div/div/div/input')

    # 点击选择角色
    # manager_role = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
    #                                    'div/div[2]/form/div[3]/div/div[2]/div/div/div/div/div[2]/input')
    manager_role = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/form/div[3]/' \
                   'div/div[2]/div/div/div/div/div[2]/span/span/i')

    '/html/body/div[3]'

    # 角色
    manager_role1 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
    manager_role2 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
    manager_role3 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[3]')
    manager_role4 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[4]')
    manager_role5 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[5]')
    manager_role6 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[6]')
    manager_role7 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[7]')


    role = [manager_role1,manager_role2,manager_role3,manager_role4,manager_role5,
            manager_role6,manager_role7]

    # 备注信息
    manager_remark = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                 'div[2]/form/div[5]/div/div[2]/div/div/div/div/textarea')

    # 点击保存
    manager_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                       'div/div[3]/div/button[2]')


    #*****************************添加管理员*****************************结束


    #*****************************点击翻页*****************************开始

    # 翻页
    next_page = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/'
                                    'div/div[2]/div/ul/li[2]')



    #*****************************点击翻页*****************************结束


    #*****************************详情*****************************开始

    # 详情
    detail = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/'
                                 'div/div[1]/div[3]/table/tbody/tr[10]/td[4]/div/span[1]')


    detail_close = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/'
                                       'div[4]/div/div[1]/button/i')
    #*****************************详情*****************************结束


    #*****************************编辑*****************************开始

    # 编辑
    edit = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/'
                               'div/div[1]/div[3]/table/tbody/tr[10]/td[4]/div/span[2]')
    # 编辑姓名
    edit_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/'
                                    'form/div[1]/div/div[2]/div/div/div/div/input')

    # 编辑手机号
    edit_phone = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/'
                                     'form/div[2]/div/div[2]/div/div/div/div/input')

    # 编辑备注信息
    edit_remark = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/'
                                      'form/div[5]/div/div[2]/div/div/div/div/textarea')


    # 点击保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[3]/'
                                    'div/button[2]')

    #*****************************编辑*****************************结束

    #*****************************删除*****************************开始

    # 删除
    delete = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/'
                                 'div[3]/table/tbody/tr[10]/td[4]/div/span[3]')

    # 删除确认
    delete_confirm = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')

    #*****************************删除*****************************结束

    name2 = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/div[3]/table/tbody/tr[10]/td[3]/div'


    #*****************************查找*****************************开始

    # 查找
    search = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[2]/button[2]')

    # 查找姓名
    search_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[1]/div/input')

    # 查找手机号
    search_phone = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/input')

    #*****************************查找*****************************结束