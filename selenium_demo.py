#!/usr/bin/python
# coding=utf-8
__author__ = 'xuchu'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

br = webdriver.Firefox()
br.implicitly_wait(30)
br.get('http://www.acfun.cn')
print br.title
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
        print handle
        br.switch_to_window(handle)
print WebDriverWait(br, 10, 0.5).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="form-login"]/div[4]/a[1]').is_displayed())


# browser.quit()

