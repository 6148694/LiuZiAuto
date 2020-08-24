#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
import pytest
import time
from pages.information_page import InformationPage,delete_account
from case.conftest import *
import allure
import urllib3
urllib3.disable_warnings()
delete_account()

@allure.title("保存留资信息")
def  test_submit_personinformation(_login):
    """登录以及填写个人资料信息"""
    driver = _login
    web = InformationPage(driver)
    web.scroll_end()
    web.click_signin()
    web.click_booking_form()
    web.submit_personinformation()
    delete_account()
    web.submit_personinformation1()
    # web.submit_education_background()
    # web.submit_work_experience()
    # web.submit_learning_object()
    # web.submit_data_upload()
    # web.submit_skill_training()
    # web.submit_honors_and_awards()
    # web.submit_i_do()







