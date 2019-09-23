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

class ProjectPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.iotrack_url
    url = home_url+'/'


    # 项目管理
    project = PageElement(xpath = '/html/body/div[1]/div/div[2]/ul/div/a[3]/li')


    #*****************************新增项目*****************************开始

    # 新增项目
    project_add = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/button')

    # 项目名称
    project_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[5]/'
                                       'div/div[2]/div/form/div[1]/div/div/input')

    # 所属机构
    project_organize = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/'
                                           'div[5]/div/div[2]/div/form/div[2]/div/div/div/input')

    # 机构
    organize1 = PageElement(xpath = '/html/body/div[3]/div[1]/div[1]/ul/li[28]')



    # 所属项目部
    project_deparment = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/'
                                            'div/div[5]/div/div[2]/div/form/div[3]/div/div/div[1]/input')

    # 项目部
    department1 = PageElement(xpath = '/html/body/div[4]/div[1]/div[1]/ul/li[1]')


    # 保存
    project_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/'
                                       'div[5]/div/div[3]/div/button[2]')

    #*****************************新增项目*****************************结束

    #*****************************搜索*****************************开始

    # 搜索
    search = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/button[2]')

    # 项目名称
    search_projectname = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[1]/'
                                             'div[1]/div/input')

    #*****************************搜索*****************************结束


    #*****************************编辑*****************************开始

    # 点击编辑
    edit = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[1]/'
                               'div[3]/table/tbody/tr/td[7]/div/span[1]')

    # 编辑项目名称
    edit_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[5]/div/'
                                    'div[2]/div/form/div[1]/div/div/input')

    # 保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[5]/div/'
                                    'div[3]/div/button[2]')

    #*****************************编辑*****************************结束


    #*****************************删除*****************************开始

    # 点击删除
    delete = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[1]/'
                                 'div[3]/table/tbody/tr/td[7]/div/span[2]')

    # 删除确认
    delete_confirm = PageElement(xpath = '/html/body/div[2]/div/div[3]/button[2]')

    #*****************************删除*****************************结束