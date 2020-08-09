#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WangLei
from common.base import Base
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
host = "https://sofia2.ezijing.com/"
#获取本地图片地址
import os
path = os.path.dirname(__file__)
path1 = os.path.dirname(path)
pic_path = os.path.join(path1,"images/pic.jpg")

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
    my_save_button_loc = ("xpath","//button[@class='btn btn-warn']")
    #个人信息-证件号码
    my_id_number_loc = ("xpath","//input[@name='id_number']")
    #个人信息-性别男
    my_sex_boy_loc = ("xpath","//input[@name='gender' and @type='radio'and @value='1']")
    #个人信息-现居城市
    my_province_loc = ("xpath","//span[@class='formsy-address']/select/option[2]")
    my_city_loc = ("xpath","//span[@class='formsy-address']/select[2]/option[2]")
    my_wechat_loc = ("xpath","//input[@name='we_chat_account']")
    my_post_address_loc = ("xpath","//input[@name='mailing_address']")
    my_emergency_contact_name_loc = ("xpath","//input[@name='emergency_contact_name']")
    my_emergency_contacts_phone_loc = ("xpath","//input[@name='emergency_contacts_phone']")
    #教育背景
    education_background_loc = ("xpath","//span[text()='教育背景']")
    school_name_loc = ("xpath","//input[@name='school_name_cn']")
    major_name_loc = ("xpath","//input[@name='major_cn']")
    xueli_loc = ("xpath","//em[@class='yes glyphicon glyphicon-ok']/../select/option[3]")
    #工作经验
    work_experience_loc = ("xpath","//span[text()='工作经验']")
    work_place_loc = ("xpath","//input[@name='company_name_cn']")
    industry_type_loc =("xpath","//em[@class='yes glyphicon glyphicon-ok']/../select/option[8]")
    work_department_loc = ("xpath","//input[@name='dept_cn']")
    work_position_loc = ("xpath","//input[@name='position_cn']")
    work_desc_loc = ("xpath","//textarea[@name='job_desc_cn']")
    #学习目的
    learning_object_loc = ("xpath","//span[text()='学习目的']")
    learning_object_cause_loc1=("xpath","//textarea[@name='question_1' and @class='formsy-textarea']")
    learning_object_cause_loc2=("xpath","//textarea[@name='question_2' and @class='formsy-textarea'] ")
    #资料上传
    data_upload_loc = ("xpath","//span[text()='资料上传']")
    #图片上传
    input_picture_loc = ("xpath","//input[@type='file' and @name = 'file']")
    button_next_loc = ("xpath","//a[text()='下一步']")
    #所受培训
    institute_cn_loc = ("xpath","//input[@name='institute_cn']")
    course_cn_loc = ("xpath","//input[@name='course_cn']")
    #荣誉和奖励
    honors_and_awards_tag_loc = ("xpath","//span[text()='荣誉奖励（可选）']")
    honors_and_awards_loc = ("xpath","//input[@label='荣誉/奖励' and @name='title']")
    get_time_loc = ("xpath","//input[@name='summary' and @label='证书颁发机构及获得时间']")

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
    def login(self,username='6148694@qq.com',password='Gaojunqing110'):
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
        self.send(self.my_phone_loc,"13088572081")
        self.send(self.my_email_loc,"6148694@qq.com")
    def submit_personinformation1(self):
        """补充个人资料"""
        self.send(self.my_id_number_loc,"152628199702022123")
        self.click(self.my_sex_boy_loc)
        self.scroll_end()
        self.click(self.my_province_loc)
        self.click(self.my_city_loc)
        self.scroll_end()
        self.send(self.my_wechat_loc,"13088572081")
        self.send(self.my_post_address_loc,"北京宋庄小堡73号")
        self.send(self.my_emergency_contact_name_loc,"小叶子")
        self.send(self.my_emergency_contacts_phone_loc,"13088572081")
        self.click(self.my_save_button_loc)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        assert '保存个人信息成功！'in  a.text
        self.js_scroll_top()
        self.js_scroll_top()
    def submit_education_background(self):
        """填写教育背景"""
        self.click(self.education_background_loc)
        self.send(self.school_name_loc,"内蒙古电子科技大学")
        self.send(self.major_name_loc,"3G移动软件开发")
        self.click(self.xueli_loc)
        self.js_scroll_end()
        self.click(self.my_save_button_loc)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        assert '保存教育信息成功！'in  a.text
        self.js_scroll_top()
    def submit_work_experience(self):
        """保存工作经验"""
        self.click(self.work_experience_loc)
        self.send(self.work_place_loc,"第三方互联网公司")
        b = self.get_text(self.industry_type_loc)
        print(b)
        self.click(self.industry_type_loc)
        self.send(self.work_department_loc,"研发部")
        self.send(self.work_position_loc,"测试工程师")
        self.send(self.work_desc_loc,"负责项目的迭代更新！")
        self.click(self.my_save_button_loc)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        assert '保存工作信息成功！'in  a.text
    def submit_learning_object(self):
        """保存学习目标"""
        self.click(self.learning_object_loc)
        self.send(self.learning_object_cause_loc1,"想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。")
        self.send(self.learning_object_cause_loc2,"开办一个世界五百强的公司，开办一个世界五百强的公司，开办一个世界五百强的公司，开办一个世界五百强的公司，开办一个世界五百强的公司，")
        self.click(self.my_save_button_loc)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        assert '保存学习目的信息成功！'in  a.text
    def  submit_data_upload(self):
        """资料上传"""
        self.click(self.data_upload_loc)
        self.send(self.input_picture_loc,pic_path)
        self.js_scroll_end()
        self.click(self.button_next_loc)
    def submit_skill_training(self):
        """所有培训填写"""
        self.send(self.institute_cn_loc,"中软国际")
        self.send(self.course_cn_loc,"安卓开发")
        self.click(self.my_save_button_loc)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        assert '保存培训信息成功！'in  a.text
    def submit_honors_and_awards(self):
        """填写荣誉奖励"""
        self.click(self.honors_and_awards_tag_loc)
        self.send(self.honors_and_awards_loc,"全市最佳标榜")
        self.send(self.get_time_loc,"2020-01-01")
        self.click(self.my_save_button_loc)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        assert '保存荣誉和奖励信息成功！'in  a.text
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get(host)
    driver.maximize_window()
    web.login()
    time.sleep(2)
    result = web.is_login_success()
    print(result)
    web.scroll_end()
    web.click_signin()
    web.click_booking_form()
    time.sleep(3)
    #填写个人信息操作
    web.submit_personinformation()
    web.submit_personinformation1()
    web.submit_education_background()
    web.submit_work_experience()
    web.submit_learning_object()
    web.submit_data_upload()
    web.submit_skill_training()
    web.submit_honors_and_awards()
    time.sleep(5)
    driver.quit()
