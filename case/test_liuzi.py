#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
import pytest
import time
from pages.login_page import LoginPage
import allure
# @allure.feature("留资信息提交")
# class TestLiuZi():
@allure.title("保存留资信息")
def  test_submit_personinformation(_login):
    """登录以及填写个人资料信息"""
    driver =_login
    time.sleep(3)
    edit = LoginPage(driver)
    edit.scroll_end()
    edit.click_signin()
    edit.click_booking_form()
    edit.submit_personinformation()
    edit.submit_personinformation1()
    edit.submit_education_background()
    edit.submit_work_experience()
    edit.submit_learning_object()
    edit.submit_data_upload()
    edit.submit_skill_training()
    edit.submit_honors_and_awards()




