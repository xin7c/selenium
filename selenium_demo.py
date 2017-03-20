#!/usr/bin/python
# coding=utf-8
__author__ = 'xuchu'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

br = webdriver.Firefox()
br.implicitly_wait(30)
br.get('http://www.acfun.cn')
now_handle = br.current_window_handle
print now_handle
br.find_element_by_xpath('//*[@id="header-guide"]/li[1]/a[2]').click()
time.sleep(3)
#获取所有窗口句柄
all_handles = br.window_handles
print all_handles
for handle in all_handles:
    if handle != now_handle:
        #输出待选择的窗口句柄
        print "即将切换到->", handle
        br.switch_to_window(handle)
driverWait = WebDriverWait(br, 10, 0.5).until(lambda x: x.find_element_by_id('ipt-account-login').is_displayed())
print "切换后的窗口标题->", br.title
if driverWait:
    print "Successed"
else:
    print "Failed"
# br.switch_to_window(all_handles[0])
print br.title
br.find_element_by_id('ipt-account-login').send_keys("18510086742")
br.find_element_by_id('ipt-pwd-login').send_keys("111111")
br.find_element_by_xpath('//*[@id="form-login"]/div[4]/a[1]').click()
# userImg = br.find_element_by_xpath('//*[@id="header-guide"]/li[1]/a[1]/img')
# userImg = br.find_element_by_xpath('//*[@id="header-guide"]/li[1]')
# print userImg
# ActionChains(br).move_to_element(userImg).perform()
WebDriverWait(br, 10, 0.5).until(lambda x: x.find_element_by_class_name('user-avatar').is_displayed())
# 准备执行JS
js = "$('.user-avatar img').mouseover()"
br.execute_script(js)
# 打印用户名
print br.find_element_by_class_name("user-name").text
br.quit()

