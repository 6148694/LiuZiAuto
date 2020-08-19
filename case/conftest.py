#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import os
import platform
#命令行参数
host_api_url = "https://sofia.ezijing.com"
delete_api_url = "https://api.ezijing.com/zws/v1/enrollment/submissions/delete"
login_api_url ="https://sofia.ezijing.com/api/passport/rest/login"
@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    if platform.system() == "Windows":
        _driver = webdriver.Chrome()
        _driver.maximize_window()
        _driver.get(host_api_url)
        print("目前是window")
    else:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动
        chrome_options.add_argument('--headless')
        _driver = webdriver.Chrome(chrome_options=chrome_options)
        _driver.get(host_api_url)
        print("目前是Linux")
    def end():
        """测试用例完成以后，执行终结函数"""
        time.sleep(3)
        _driver.quit()
    request.addfinalizer(end)
    return _driver
@pytest.fixture(scope="session")
def _login(driver):
    """前置条件登录"""
    web = LoginPage(driver)
    web.login()
    return driver
