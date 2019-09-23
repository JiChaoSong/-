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

class JobManagePage(PageObject):

    # 当前测试页面的测试网址url
    home_url = Url.organize_url
    url = home_url+'/'

    # 系统管理
    sysmanage = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[6]/div')

    # 岗位管理
    jobmanage = PageElement(xpath = '/html/body/div[1]/div[1]/div[2]/ul/div/li[6]/ul/a[2]/li')

    #*****************************新增岗位*****************************开始

    # 点击新建岗位
    job_add = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[2]/button')

    # 岗位姓名
    job_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                   'div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')

    # pc端
    job_pc = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/div[2]/form/'
                                 'div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/label/span[1]/span')

    # app
    job_app = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/div/'
                                  'div[2]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/label/span[1]/span')

    # 保存
    job_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                   'div[4]/div/div[3]/div/button[2]')

    #*****************************新增岗位*****************************结束


    #*****************************岗位详情*****************************开始

    jobname = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/' \
              'div/div[1]/div[3]/table/tbody/tr/td[1]/div'

    # 点击详情
    detail = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/'
                                 'div/div[1]/div[3]/table/tbody/tr/td[3]/div/span[1]')

    # 岗位名称
    detail_name = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/' \
                  'div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/span'

    # 关闭
    detail_close = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/'
                                       'div/div/div/div[4]/div/div[1]/button/i')

    #*****************************岗位详情*****************************结束


    #*****************************岗位编辑*****************************开始

    # 点击编辑
    edit = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                               'div[3]/div/div[1]/div[3]/table/tbody/tr/td[3]/div/span[2]')

    # 编辑名称
    edit_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                    'div[4]/div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')

    # 编辑保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                    'div[4]/div/div[3]/div/button[2]')
    
    #*****************************岗位编辑*****************************结束
    
    #*****************************删除*****************************开始

    # 点击删除
    delete = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                 'div[3]/div/div[1]/div[3]/table/tbody/tr/td[3]/div/span[3]')

    # 删除确认
    delete_confirm = PageElement(css = 'html body.el-popup-parent--hidden div.el-message-box__wrapper div.'
                                       'el-message-box div.el-message-box__btns button.el-button.el'
                                       '-button--default.el-button--small.el-button--primary')

    #*****************************删除*****************************结束
    