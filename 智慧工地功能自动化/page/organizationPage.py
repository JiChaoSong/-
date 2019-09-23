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

class OrganizePage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.iotrack_url
    url = home_url+'/'


    #*****************************机构新增*****************************开始

    # 新增
    add_organize = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/button')

    # 添加图片
    add_logo = PageElement(xpath = '//*[@id="up-con"]')

    # 机构名称
    add_organize_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                            'div/div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/input')

    # 机构所属企业
    add_organize_company = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                            'div/div[2]/form/div[4]/div/div[2]/div/div/div[1]/div/input')

    # 组织代码
    add_organize_code = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                            'div[2]/form/div[5]/div/div[2]/div/div/div[1]/div/input')

    # 行业
    add_organize_hangye = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                              'div[2]/form/div[6]/div/div[2]/div/div/div[1]/div/input')

    # 有效期
    add_organize_starttime = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                                 'div[2]/form/div[7]/div/div[2]/div/div/div[1]/div/input[1]')

    add_organize_endtime = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                               'div[2]/form/div[7]/div/div[2]/div/div/div[1]/div/input[2]')

    # 员工数量
    add_organize_num = PageElement(xpath ='/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/'
                                          'form/div[8]/div/div[2]/div/div/div/div/input')

    # 机构描述
    add_organize_depict = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                              'div[2]/form/div[9]/div/div[2]/div/div/div/div/textarea')

    # 机构负责人
    add_organize_person = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                              'div[2]/form/div[11]/div/div[2]/div/div/div[1]/div/input')

    # 电话
    add_organize_phone = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/'
                                             'div[2]/form/div[12]/div/div[2]/div/div/div[1]/div/input')

    # 保存
    add_organize_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/'
                                            'div[4]/div/div[3]/div/button[2]')

    #*****************************机构新增*****************************结束


    #*****************************项目配置*****************************开始

    # 搜索负责人姓名
    search_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/input')

    search_phone = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[3]/div/input')

    # 点击搜索
    search = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[2]/button[2]')

    # 断言
    name_assert = ''

    # 翻页
    next_page = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/'
                                    'div/div[3]/div/div[2]/div/ul/li[4]')

    # 项目配置
    # project_set = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/'
    #                                   'div/div[1]/div[3]/table/tbody/tr[7]/td[9]/div/span[1]')

    project_set = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/'
                                      'div/div[1]/div[3]/table/tbody/tr/td[9]/div/span[1]')

    # PC端
    PC = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/'
                             'form/div/div/div[2]/div/div/div/div[2]/div[1]/div/label/span[1]/span')

    # APP
    APP = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[2]/'
                              'form/div/div/div[2]/div/div/div/div[2]/div[2]/div/label/span[1]/span')

    # 保存
    project_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/'
                                       'div[4]/div/div[3]/div/button[2]')

    #*****************************项目配置*****************************结束

    #*****************************详情*****************************开始

    # 点击详情
    detail = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/div/'
                                 'div[1]/div[3]/table/tbody/tr/td[9]/div/span[2]')

    detail_close = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/div/div[1]/button/i')
    
    #*****************************详情*****************************结束
    
    
    #*****************************编辑*****************************开始

    # 点击编辑
    edit = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/'
                               'div/div[1]/div[3]/table/tbody/tr/td[9]/div/span[3]')
    # 点击编辑项目部名称
    edit_name = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                    'div/div[2]/form/div[3]/div/div[2]/div/div/div/div/input')

    edit_company = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                       'div/div[2]/form/div[4]/div/div[2]/div/div/div/div/input')

    edit_code = PageElement(xpath= '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                   'div/div[2]/form/div[5]/div/div[2]/div/div/div/div/input')

    edit_hangye = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                      'div/div[2]/form/div[6]/div/div[2]/div/div/div/div/input')

    edit_starttime = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                         'div/div[2]/form/div[7]/div/div[2]/div/div/div/div/input[1]')

    edit_endtime = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                       'div/div[2]/form/div[7]/div/div[2]/div/div/div/div/input[2]')

    edit_num = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                   'div/div[2]/form/div[8]/div/div[2]/div/div/div/div/input')

    edit_descipt = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                       'div/div[2]/form/div[9]/div/div[2]/div/div/div/div/textarea')

    edit_person = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                      'div/div[2]/form/div[11]/div/div[2]/div/div/div/div/input')

    edit_phone = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                     'div/div[2]/form/div[12]/div/div[2]/div/div/div/div/input')

    edit_save = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[4]/'
                                    'div/div[3]/div/button[2]')

    phone = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/div[3]/table/tbody/tr/td[8]/div'

    #*****************************编辑*****************************结束
    
    #*****************************删除*****************************开始

    # 点击删除
    delete = PageElement(xpath = '/html/body/div[1]/div/div[3]/section/div[2]/div/div/div[3]/div/div[1]/'
                                 'div[3]/table/tbody/tr/td[9]/div/span[4]')

    # 删除确认
    delete_confirm = PageElement(css = 'html body.el-popup-parent--hidden div.el-message-box_'
                                       '_wrapper div.el-message-box'
                                       ' div.el-message-box__btns button.el-button.el-button-'
                                       '-default.el-button--small.el-button--primary')

    #*****************************删除*****************************结束