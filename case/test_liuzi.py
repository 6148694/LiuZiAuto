#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
import pytest
import time
from pages.login_page import LoginPage,delete_account,host
import allure
from selenium import webdriver
import urllib3
urllib3.disable_warnings()
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def is_windows_linux():
    '''判断当前系统是windows还是linux:
    一般linux结果为('32bit','ELF')ELF或者('64bit','ELF')ELF，
    windows为('32bit','windowsPE')或者('64bit','windowsPE')'''
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    #  可以先判断是否启动无界面
    chrome_options.add_argument('--headless')  # 无界面
    if "win" not in sys.platform:
        print("当前运行的操作系统是Linux,请确认是操作系统是否判断正确")
    else:
        print("当前运行的操作系统是Windows,请确认是操作系统是否判断正确")
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
@allure.title("保存留资信息")
def  test_submit_personinformation():
    """登录以及填写个人资料信息"""
    driver = is_windows_linux()
    driver.get(host)
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    time.sleep(2)
    result = web.is_login_success()
    print(result)
    web.scroll_end()
    web.click_signin()
    web.click_booking_form()
    web.submit_personinformation()
    web.submit_personinformation1()
    web.submit_education_background()
    web.submit_work_experience()
    web.submit_learning_object()
    web.submit_data_upload()
    web.submit_skill_training()
    web.submit_honors_and_awards()
    web.submit_i_do()
    delete_account()






