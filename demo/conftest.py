#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
import pytest
import allure
@allure.step("登录步骤1：输入账号")
def step1():
    print("请输入账号")
@allure.step("登录步骤2：请输入密码")
def step2():
    print("请输入密码")
@allure.step("登录步骤3：点击登录")
def step3():
    print("点击登录")


@pytest.fixture(scope="session")
def login():
    print("登录操作")
    step1()
    step2()
    step3()
