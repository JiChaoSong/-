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
    home_url = Url.organize_url
    url = home_url+'/'

    name = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/' \
           'div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'

    name1 = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/' \
            'div/div[1]/div[3]/table/tbody/tr/td[1]/div'

    #*****************************新增*****************************开始

    # 新增
    add_organize = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[1]/button')

    # 项目部名称
    add_organize_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                            'div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')

    # 总包公司
    add_organize_zb = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                          'div/div[2]/form/div[2]/div/div[2]/div/div/div[1]/div/input')

    # 信用代码
    add_organize_code = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                            'div/div[2]/form/div[3]/div/div[2]/div/div/div[1]/div/input')

    # 开户行
    add_organize_bank = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                            'div/div[2]/form/div[4]/div/div[2]/div/div/div[1]/div/input')

    # 卡号
    add_organize_banknum = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                               'div/div[2]/form/div[5]/div/div[2]/div/div/div[1]/div/input')

    # 负责人
    add_organize_person = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                              'div/div[2]/form/div[6]/div/div[2]/div/div/div[1]/div/input')

    # 手机号
    add_organize_phone = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                             'div/div[2]/form/div[7]/div/div[2]/div/div/div[1]/div/input')

    # 保存
    add_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/'
                                   'div/div[3]/div/button[2]')

    #*****************************新增*****************************结束


    #*****************************详情*****************************开始

    # 点击查看
    detail = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/'
                                 'section/div/div/div/div[3]/div/div[1]/div[3]/table/tbody/tr/td[4]/div/span[1]')

    # 点击关闭
    detail_close = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/'
                                       'div/div[4]/div/div[1]/button/i')

    # 详情名称
    detail_name = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[4]/' \
                  'div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/span'

    #*****************************详情*****************************结束

    #*****************************编辑*****************************开始

    # 编辑
    edit = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[3]/'
                               'div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/span[2]')

    # 项目部名称
    edit_organize_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/'
                                             'div[4]/div/div[2]/form/div[1]/div/div[2]/div/div/div[1]/div/input')


    # 保存
    edit_save = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/'
                                    'div/div[4]/div/div[3]/div/button[2]')
    #*****************************编辑*****************************结束


    #*****************************删除*****************************开始

    # 删除
    delete = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/'
                                 'div/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/span[3]')

    # 删除确认
    delete_confirm = PageElement(css = 'body > div.el-message-box__wrapper > div > div.el-message-box__btns >'
                                       ' button.el-button.el-button--default.el-button--small.el-button--primary')

    #*****************************删除*****************************结束


    #*****************************搜索*****************************开始

    search_name = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/'
                                 'div/div/div/div[1]/div[1]/div/input')

    search = PageElement(xpath = '/html/body/div[1]/div[1]/div[3]/div/div/section/div/div/div/div[2]/button[2]')


    #*****************************搜索*****************************结束