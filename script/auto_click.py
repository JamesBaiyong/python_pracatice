#encoding=utf-8
from selenium import webdriver
import time

path = './chrome_driver/chromedriver'

dri = webdriver.Chrome(path)
dri.implicitly_wait(10)
dri.get('http://www.xxxxx.com.cn/xxxx-new/information/companylist')
time.sleep(2)
dri.find_element_by_link_text(u'某某主板').click()
time.sleep(2)
x = dri.find_elements_by_xpath('//*[@id="con-a-1"]/ul/li')

for i in x:
    print(i.text)
    i.click()
    time.sleep(2)
    # 浏览器句柄
    handles = dri.window_handles
    print handles
    # 切换到新开窗口句柄
    dri.switch_to.window(handles[-1])
    # 关闭新开窗口句柄
    dri.close()
    dri.switch_to.window(handles[0])

dri.quit()