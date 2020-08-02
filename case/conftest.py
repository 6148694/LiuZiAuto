#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
@pytest.fixture(scope="session")
def driver(request):
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    _driver.get("https://sofia2.ezijing.com/api/passport/rest/login")

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
