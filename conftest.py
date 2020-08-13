#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
#命令行参数
def pytest_addoption(parser):
    """添加命令行参数"""
    parser.addoption(
                '--headless', action="store",
                 default='no', help='set chrome headless option yes or no'
    )
@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    if headless=="yes":
        chrome_options.add_argument('--headless')  # 无界面
    _driver = webdriver.Chrome(chrome_options=chrome_options)
    _driver.maximize_window()
    _driver.get("https://sofia2.ezijing.com/")
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
