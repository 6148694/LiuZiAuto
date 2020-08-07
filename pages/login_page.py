#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from common.base import Base
import time
from selenium.webdriver.support.select import Select
host = "https://sofia2.ezijing.com/"
# login_url = host+"/login"
class   LoginPage(Base):
    """登录页面"""
    #首页登录入口提示
    login_tag_loc = ("xpath","//*[text()='登录']")
    #首页登录用户名
    username_loc = ("xpath","//input[@name='account' ]")
    #首页登录密码
    password_loc = ("xpath","//input[@name='password']")
    #首页登录按钮
    login_button_loc = ("xpath","//button[@type='submit']")
    #登录后的文字校验
    success_login_loc = ("xpath","//*[text()='系统首页']")
    #首页的报名申请
    signin_tag_loc =  ("xpath","//div[@class='col-xs-6 col-sm-4 col-md-4']")
    #填写报名表
    booking_form_tag_loc =("xpath","//*[text()='填写报名表']")
    #个人信息-姓名
    my_name_loc = ("xpath","//input[@name='real_name_cn']")
    #个人信息-手机号码
    my_phone_loc=("xpath","//input[@name='phone_number']")
    #个人信息-邮件
    my_email_loc=("xpath","//input[@name='email']")
    #个人信息-保存按钮
    my_save_button_loc = ("xpath","//button[@class='btn btn-warn' and @type ='submit']")
    #个人信息-证件号码
    my_id_number_loc = ("xpath","//input[@name=id_number]")
    #个人信息-性别男
    my_sex_boy_loc = ("xpath","//input[@name='gender' and @type='radio'and @value='1']")
    #个人信息-现居城市
    my_city_loc = ("xpath","//select[@]")
    ".//*[@id='nr']/option[2]"

    def click_login_tag(self):
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
    def login(self,username='18501201225',password='Gaojunqing110'):
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
    def submit_personinformation(self):
        """首次提交个人信息"""
        self.send(self.my_name_loc,"测试")
        self.send(self.my_phone_loc,"18501201225")
        self.send(self.my_email_loc,"18501201225@qq.com")
        self.click(self.my_save_button_loc)
    def submit_personinformation1(self):
        """补充个人资料"""
        self.send(self.my_id_number_loc,"152628199402022123")
        self.click(self.my_sex_boy_loc)
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
    #填写个人信息操作
    web.submit_personinformation()
    web.submit_personinformation1()
    time.sleep(5)
    driver.quit()
