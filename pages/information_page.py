# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 10:45
# @Author  : WangLei
from common.base import Base
import time
import os
import requests
import urllib3
from case.conftest import *
urllib3.disable_warnings()
import allure
#获取本地图片地址
path = os.path.dirname(__file__)
path1 = os.path.dirname(path)
pic_path = os.path.join(path1,"images/pic.jpg")
def delete_account():
    login_body={
        "account":"6148694@qq.com",
        "password":"Gaojunqing110",
        "RememberMe":"1",
        "rd":"%2F",
        "service":"https://sofia.ezijing.com"
    }
    delete_body ={
        "project_id":1000
    }
    s = requests.session()
    result = s.post(login_api_url,data=login_body,verify=False)
    print(result.text)
    DeleteResult = s.post(delete_api_url,data=delete_body,verify=False)
    print(DeleteResult.text)
    print("************************************************数据已清理**************************************************************")

class   InformationPage(Base):
    """填写留资信息"""
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
    #有效身份证件（正面）
    input_picture_loc = ("xpath","//input[@type='file' and @name = 'file']")
    #有效身份证件（反面）
    input_picture1_loc = ("xpath","//div[@id='up_05']/div/input")
    #毕业证书
    input_picture2_loc = ("xpath","//div[@id='up_03']/div/input")
    #学位证书
    input_picture3_loc = ("xpath","//div[@id='up_04']/div/input")
    button_next_loc = ("xpath","//a[text()='下一步']")
    #所受培训
    institute_cn_loc = ("xpath","//input[@name='institute_cn']")
    course_cn_loc = ("xpath","//input[@name='course_cn']")
    #荣誉和奖励
    honors_and_awards_tag_loc = ("xpath","//span[text()='荣誉奖励（可选）']")
    honors_and_awards_loc = ("xpath","//input[@label='荣誉/奖励' and @name='title']")
    get_time_loc = ("xpath","//input[@name='summary' and @label='证书颁发机构及获得时间']")
    #返回报名系统
    back_os_loc = ("xpath","//a[@class='return fr']")
    #提交审核
    submit_loc = ("xpath","//a[text()='提交']")
    i_do_loc = ("xpath","//input[@type='radio' and @name='agree']")
    i_submit_loc = ("xpath","//button[@class='btn-red' and @type='submit']")
    @allure.step("滚动到底部")
    def scroll_end(self):
        """滚动到底部"""
        self.js_scroll_end()
    @allure.step("点击报名申请")
    def click_signin(self):
        """点击报名申请"""
        self.click(self.signin_tag_loc)
    @allure.step("点击填写报名表")
    def click_booking_form(self):
        """点击填写报名表"""
        self.click(self.booking_form_tag_loc)
        time.sleep(1)
    @allure.step("首次提交个人信息")
    def submit_personinformation(self):
        """首次提交个人信息"""
        self.send(self.my_name_loc,"测试小王")
        self.send(self.my_phone_loc,"13088572088")
        self.send(self.my_email_loc,"313035600@qq.com")
    @allure.step("补充个人资料")
    def submit_personinformation1(self):
        """补充个人资料"""
        self.send(self.my_id_number_loc,"152628199702022188")
        self.click(self.my_sex_boy_loc)
        self.scroll_end()
        self.click(self.my_province_loc)
        self.click(self.my_city_loc)
        self.scroll_end()
        self.send(self.my_wechat_loc,"13088572088")
        self.send(self.my_post_address_loc,"北京宋庄小堡73号")
        self.send(self.my_emergency_contact_name_loc,"小叶子")
        self.send(self.my_emergency_contacts_phone_loc,"13088572088")
        self.click(self.my_save_button_loc)
        time.sleep(2)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        self.js_scroll_top()
        self.js_scroll_top()
    @allure.step("填写教育背景")
    def submit_education_background(self):
        """填写教育背景"""
        self.click(self.education_background_loc)
        self.send(self.school_name_loc,"内蒙古电子科技大学")
        self.send(self.major_name_loc,"3G移动软件开发")
        self.click(self.xueli_loc)
        self.js_scroll_end()
        self.click(self.my_save_button_loc)
        time.sleep(2)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        self.js_scroll_top()
    @allure.step("保存工作经验")
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
        time.sleep(2)
        a = self.switch_alert()
        print(a.text)
        a.accept()
    @allure.step("保存学习目标")
    def submit_learning_object(self):
        """保存学习目标"""
        self.click(self.learning_object_loc)
        self.send(self.learning_object_cause_loc1,"想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。想要从事工商管理类职业，能力突破。")
        self.send(self.learning_object_cause_loc2,"开办一个世界五百强的公司，开办一个世界五百强的公司，开办一个世界五百强的公司，开办一个世界五百强的公司，开办一个世界五百强的公司，")
        self.click(self.my_save_button_loc)
        time.sleep(2)
        a = self.switch_alert()
        print(a.text)
        a.accept()
    @allure.step("资料上传")
    def  submit_data_upload(self):
        """资料上传"""
        self.click(self.data_upload_loc)
        time.sleep(1)
        self.send(self.input_picture_loc,pic_path)
        self.js_scroll_end_2()
        time.sleep(1)
        self.send(self.input_picture1_loc,pic_path)
        self.js_scroll_end_1()
        time.sleep(1)
        self.send(self.input_picture2_loc,pic_path)
        self.js_scroll_end()
        time.sleep(1)
        self.send(self.input_picture3_loc,pic_path)
        time.sleep(3)
        self.click(self.button_next_loc)
    @allure.step("所有培训填写")
    def submit_skill_training(self):
        """所有培训填写"""
        self.send(self.institute_cn_loc,"中软国际")
        self.send(self.course_cn_loc,"安卓开发")
        self.click(self.my_save_button_loc)
        time.sleep(2)
        a = self.switch_alert()
        print(a.text)
        a.accept()
    @allure.step("填写荣誉奖励")
    def submit_honors_and_awards(self):
        """填写荣誉奖励"""
        self.click(self.honors_and_awards_tag_loc)
        self.send(self.honors_and_awards_loc,"全市最佳标榜")
        self.send(self.get_time_loc,"2020-01-01")
        self.click(self.my_save_button_loc)
        time.sleep(2)
        a = self.switch_alert()
        print(a.text)
        a.accept()
        self.click(self.back_os_loc)
    @allure.step("同意协议，提交信息表")
    def submit_i_do(self):
        """我同意"""
        self.click(self.submit_loc)
        self.click(self.i_do_loc)
        self.click(self.i_submit_loc)
if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage
    delete_account()
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.maximize_window()
    web.login()
    result = web.is_login_success()
    print(result)
    web.scroll_end()
    print('向下滚动')
    web.click_signin()
    print('点击报名申请')
    web.click_booking_form()
    print('点击填写报名表')
    time.sleep(2)
    #填写个人信息操作
    web.submit_personinformation()
    print('填写个人信息')
    web.submit_personinformation1()
    web.submit_education_background()
    web.submit_work_experience()
    web.submit_learning_object()
    web.submit_data_upload()
    web.submit_skill_training()
    web.submit_honors_and_awards()
    web.submit_i_do()
    time.sleep(5)
    driver.quit()