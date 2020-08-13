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
@allure.title("保存留资信息")
def  test_submit_personinformation():
    """登录以及填写个人资料信息"""
    driver = webdriver.Chrome()
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






