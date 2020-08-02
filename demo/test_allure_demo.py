#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
import pytest
import allure
@allure.step("用例步骤1")
def step_1():
     print("用例步骤1")
@allure.step("用例步骤2")
def step_2():
     print("用例步骤2")
@allure.step("用例步骤3")
def step_3():
     print("用例步骤3")
@allure.feature("功能模块1")
class TestDemo():
    "登录功能模块描述"
    @allure.title("测试用例1")
    def test_1(self,login):
        step_1()
    @allure.story("测试用例2")
    def test_2(self,login):
        step_2()
    @allure.title("测试用例3title")
    def test_3(self,login):
        step_1()
        step_2()
        step_3()
