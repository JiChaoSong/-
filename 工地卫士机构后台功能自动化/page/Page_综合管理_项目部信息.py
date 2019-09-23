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

class DepartmentInfoPage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.organize_url
    url = home_url+'/'

    # 综合管理
    intergrated_management = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[4]/div')

    # 项目部信息
    department_info = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[4]/ul/a[1]/li')

    # 项目管理
    project_management = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[4]/ul/a[2]/li')

    # 设备管理
    device_management = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[4]/ul/a[3]/li')

    # 大屏管理
    screen_management = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[4]/ul/a[4]/li')
    
    #*****************************项目部信息*****************************开始

    # 项目部名称
    department_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                          'form/div[1]/div/div[2]/div/div/div[1]/div/input')

    # 总包公司
    department_company = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/'
                                             'div/form/div[2]/div/div[2]/div/div/div[1]/div/input')

    # 代码
    department_code = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                          'form/div[3]/div/div[2]/div/div/div[1]/div/input')

    # 开户行
    department_bank = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                          'form/div[4]/div/div[2]/div/div/div[1]/div/input')

    # 卡号
    department_banknum = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                             'form/div[5]/div/div[2]/div/div/div[1]/div/input')

    # 人员采集设备编号
    person_device_code = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                             'form/div[6]/div/div[2]/div/div/div[1]/div/input')

    # 保存
    department_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div/button')
    #*****************************项目部信息*****************************结束


