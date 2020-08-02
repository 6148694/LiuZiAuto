#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from common.base import Base
import time
host = "https://sofia2.ezijing.com/api/passport/rest"
login_url = host+"/login"
class   LoginPage(Base):
    """登录页面"""
    loc1 = ("name","account")
    loc2 = ("name","password")
    loc3 = ("css","#panel-login>div.panel-body>button")
    loc4 = ("css","#top-nav>div.navbar-header>a")
    def input_user(self,username):
        """输入账号"""
        self.send(self.loc1,username)
    def input_password(self,password):
        """输入密码"""
        self.send(self.loc2,password)
    def click_button(self):
        """点击登录"""
        self.click(self.loc3)
    def login(self,username='111',password='gaojunqing110'):
        """登录流程"""
        self.input_user(username)
        self.input_password(password)
        self.click_button()
    def is_login_success(self):
        """判断是否登录成功，返回bool值"""
        text = self.get_text(self.loc4)
        print("登录完成后，获取页面文本元素{}".format(text))

        return text == "秦芳影视化妆项目管理系统"
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get(login_url)
    web.login()
    time.sleep(3)
    result = web.is_login_success()
    print(result)
    driver.quit()
