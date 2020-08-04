#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from common.base import Base
import time
host = "https://sofia2.ezijing.com/"
# login_url = host+"/login"
class   LoginPage(Base):
    """登录页面"""
    login_tag_loc = ("xpath","//*[text()='登录']")
    username_loc = ("xpath","//input[@name='account' ]")
    password_loc = ("xpath","//input[@name='password']")
    login_button_loc = ("xpath","//button[@type='submit']")
    success_login_loc = ("xpath","//*[text()='系统首页']")
    signin_tag_loc =  ("xpath","//span[@href='/apply']")
    booking_form_tag_loc =("xpath","//*[text()='填写报名表']")
    def click_login_tag(self,):
        """点击登录Tag"""
        self.click(self.login_tag_loc)
    def input_user(self,username):
        """输入账号"""
        self.send(self.username_loc,username)
    def input_password(self,password):
        """输入密码"""
        self.send(self.password_loc,password)
    def click_button(self):
        """点击登录"""
        self.click(self.login_button_loc)
    def login(self,username='18501057611',password='Gaojunqing110'):
        """登录流程"""
        self.click_login_tag()
        self.input_user(username)
        self.input_password(password)
        self.click_button()
    def is_login_success(self):
        """判断是否登录成功，返回bool值"""
        text = self.get_text(self.success_login_loc)
        print("登录完成后，获取页面文本元素是:{}".format(text))
        return text == "系统首页"
    def scroll_end(self):
        """滚动到底部"""
        self.js_scroll_end()
    def click_signin(self):
        """点击报名申请"""
        self.click(self.signin_tag_loc)
    def click_booking_form(self):
        """点击填写报名表"""
        self.click(self.booking_form_tag_loc)
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get(host)
    driver.maximize_window()
    web.login()
    time.sleep(4)
    result = web.is_login_success()
    print(result)
    web.scroll_end()
    web.click_signin()
    web.click_booking_form()
    time.sleep(5)
    driver.quit()
