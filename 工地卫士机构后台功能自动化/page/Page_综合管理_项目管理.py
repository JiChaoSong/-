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

class ProjectmanagePage(PageObject):

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
    
    
    
    #*****************************详情*****************************开始

    detail = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                 'div/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]')


    #*****************************详情*****************************结束

    #*****************************项目地图*****************************开始

    # 点击项目地图
    project_map = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                      'div[4]/div/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/span[2]')

    # 点击上传地图
    upload_map = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                     'div[2]/div[3]/div[2]/span/button')

    #*****************************项目地图*****************************结束


    #*****************************编辑*****************************开始

    # 点击编辑
    edit = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                               'div/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/span[3]')


    # 项目名称
    edit_projectname = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/'
                                           'div/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[2]/'
                                           'div/div/div[1]/div/input')

    # 工程名称
    edit_engineeringname = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/'
                                               'div/div/div[5]/div/div[2]/div/div[2]/form/div[2]/div/'
                                               'div[2]/div/div/div[1]/div/input')

    # 许可证编号
    premit_code = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/'
                                      'div/div[2]/div/div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/input')

    # 总包公司
    edit_company = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/'
                                       'div/div[2]/div/div[2]/form/div[4]/div/div[2]/div/div/div[1]/div/input')

    # 总包 信用代码
    edit_companycode= PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/'
                                          'div/div[2]/div/div[2]/form/div[5]/div/div[2]/div/div/div[1]/div/input')

    # 项目状态
    edit_projectstatus = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/'
                                             'div/div[2]/div/div[2]/form/div[6]/div/div[2]/div/div/div[1]/'
                                             'div/div/span/span/i')

    # 状态选择
    statu1 = PageElement(xpath = '/html/body/div[5]/div[1]/div[1]/ul/li[3]')

    # 项目区域
    edit_projectaddress = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/'
                                              'div/div[2]/div/div[2]/form/div[7]/div/div[2]/div/div/div[1]/div/div/'
                                           'input')
    adr1 = PageElement(xpath= '/html/body/div[6]/div[1]/div[1]/div[1]/ul/li/i')
    adr2 = PageElement(xpath= '/html/body/div[6]/div[1]/div[2]/div[1]/ul/li/i')
    adr3 = PageElement(xpath= '/html/body/div[6]/div[1]/div[3]/div[1]/ul/li/i')
    adr4 = PageElement(xpath= '/html/body/div[6]/div[1]/div[4]/div[1]/ul/li[1]/span')


    # 工程类别
    project_type = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                       'div[2]/div/div[2]/form/div[8]/div/div[2]/div/div/div[1]/div/div/input')

    # 类别选择
    type1 = PageElement(xpath = '/html/body/div[7]/div[1]/div[1]/ul/li[1]')
    # '/html/body/div[10]/div[1]/div[1]/ul/li[1]'

    # 建筑用途
    organizePurposeType = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                              'div[5]/div/div[2]/div/div[2]/form/div[9]/div/div[2]/div/div/'
                                              'div[1]/div/div/input')
    # 建筑类型选择
    PurposeType = PageElement(xpath = '/html/body/div[8]/div[1]/div[1]/ul/li[1]')

    # 项目负责人

    responsorName = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]'
                                         '/div/div[2]/div/div[2]/form/div[11]/div/div[2]/div/div/div[1]/'
                                         'div/input')

    # 负责人联系方式
    responsorPhone = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]'
                                         '/div/div[2]/div/div[2]/form/div[12]/div/div[2]/div/div/div[1]/'
                                         'div/input')

    starttime = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                    'div[2]/div/div[2]/form/div[13]/div/div[2]/div/div/div[1]/div/input')

    endtimt = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                  'div[2]/div/div[2]/form/div[14]/div/div[2]/div/div/div[1]/div/input')

    # 上传平面图
    upload_pingmian =  PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                           'div[5]/div/div[2]/div/div[2]/form/div[15]/div/div[2]/div/div/div[1]')

    # 点击选择位置
    place = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                'div[2]/div/div[2]/form/div[16]/div[3]/button')

    # 建筑面积
    buildingArea = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                       'div[5]/div/div[2]/div/div[2]/form/div[10]/div/div[2]/div/div/div[1]/div/input')


    # 输入地址
    inputaddress= PageElement(xpath = '//*[@id="suggestId"]')

    # 点击搜搜
    click_search = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[6]/div/div[2]/div/div/div/div[2]/i')

    # 点击确认
    address_confirm = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                          'div[6]/div/div[3]/div/button[2]')
    # 杭州市西湖区中天.-MCCB座
    # appid
    mAPPID = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                 'div[2]/div/div[2]/form/div[17]/div/div[2]/div/div/div[1]/div/input')

    # KEY
    APPKEY = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]/div/'
                                 'div[2]/div/div[2]/form/div[18]/div/div[2]/div/div/div[1]/div/input')

    # 点击保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[5]'
                                    '/div/div[3]/div/button[2]')

    #*****************************编辑*****************************结束