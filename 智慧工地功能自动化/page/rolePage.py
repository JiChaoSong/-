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

class RolePage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.iotrack_url
    url = home_url+'/'


    #*****************************角色新增*****************************开始

    # 点击切换到角色管理模块
    role = PageElement(xpath = '/html/body/div/div/div[2]/ul/div/a[6]/li')

    # 点击新增
    add_role = PageElement(xpath = '/html/body/div/div/div[3]/section/div[2]/div/div/button')

    # 角色名称
    role_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                    'div/div[2]/form/div[1]/div/div[2]/div/div/div/div/input')

    # 点击分配所有权限
    all_quanxian = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                       'div/div[2]/form/div[2]/div/div[2]/div/div/div/div/label/span[1]/span')

    # 点击保存
    save_role = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                    'div/div[3]/div/button[2]')

    # 权限名称元素
    save_name = '/html/body/div/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'

    #*****************************角色新增*****************************结束

    #*****************************角色详情*****************************开始

    # 点击查看详情（默认选择第一个）
    role_detail = PageElement(xpath = '/html/body/div/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/'
                                      'div[3]/table/tbody/tr[1]/td[3]/div/span[1]')

    # # 第一个name
    # list_name = ''

    # 角色详情名称元素
    detail_name = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/form/div[1]/div/div[2]/div/div/div/div/input'

    #*****************************角色详情*****************************结束


    #*****************************角色编辑*****************************开始

    # 点击编辑角色
    edit_role = PageElement(xpath = '/html/body/div/div/div[3]/section/div[2]/div/div/div[3]/div/'
                                    'div[1]/div[3]/table/tbody/tr[1]/td[3]/div/span[2]')

    # 编辑角色名称
    edit_role_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                         'div/div[2]/form/div[1]/div/div[2]/div/div/div/div/input')

    # 点击保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                    'div[3]/div/button[2]')

    #*****************************角色编辑*****************************结束


    #*****************************角色删除*****************************开始

    # 角色删除
    del_role = PageElement(xpath = '/html/body/div/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/'
                                   'div[3]/table/tbody/tr[1]/td[3]/div/span[3]')

    # 删除确认
    del_confirm = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')

    #*****************************角色删除*****************************结束

