from selenium import webdriver
drv = webdriver.Chrome('chromedriver.exe')
drv.implicitly_wait(3)
drv.get('https://nid.naver.com/nidlogin.login')
drv.find_element_by_name('id').send_keys('id1234')
drv.find_element_by_name('pw').send_keys('pw1234')
drv.find_element_by_class_name('btn_global').click()
drv.close()
