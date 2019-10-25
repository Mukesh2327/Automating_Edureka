from selenium import webdriver
import random
import time # as selenium works only when whole page is loaded
from selenium.webdriver.common.keys import Keys
#creating a browser instance for chrome for testing
browser=webdriver.Chrome() 
#going to edureka official website
browser.get('https://www.edureka.co')
time.sleep(7)
#getting the link for opening the login tab
browser.find_element_by_link_text('Log In').click()
time.sleep(5)
#getting the mail input type element from the login box
mail=browser.find_element_by_id('si_popup_email')
mail.send_keys('Test123@gmail.com')
#getting the password input type element from the login box
password=browser.find_element_by_id('si_popup_passwd')
#reading password from a file
with open('test.txt', 'r') as myfile:   
    Password = myfile.read().replace('\n', '') 
#sending password to password field
password.send_keys(Password)
#login button
LOG=browser.find_element_by_xpath("//button[@class='clik_btn_log btn-block']")
LOG.click()
time.sleep(10)
#clicking on image icon of user to make visible list of option inside it
browser.find_element_by_xpath("//a[@class='dropdown-toggle trackButton']//img[@class='img30']").click()
time.sleep(3)
# selecting my profile from list of option in image icon of user
browser.find_element_by_xpath("//ul[@class='dropdown-menu user-menu profile-xs hidden-sm hidden-xs']//a[@class='giTrackElementHeader'][contains(text(),'My Profile')]").click()
time.sleep(10)
#going to personal details page
browser.find_element_by_class_name("icon-pr-edit").click()
time.sleep(10)
#returning back from personal details page to my profile page
browser.find_element_by_class_name("icon-Arrow-Left").click()
time.sleep(3)
#dropdown arrow selection in my profile page
browser.find_element_by_class_name("icon-down-arrow2").click()
time.sleep(4)
#selecting all courses page
browser.find_element_by_xpath('//*[@id="footauto"]/app-root/app-profile-main/app-header/header/nav/div/div[3]/ul/li[2]/div/ul/li[2]/a').click()
time.sleep(6)
#selecting any ramdom 1-7 anchor tag in all courses page
browser.find_element_by_xpath('/html/body/section[3]/div[2]/div[2]/div[2]/div[1]/div[2]/a["random.randint(1,7)"]').click()
time.sleep(10)
#coming back to all courses page
browser.find_element_by_xpath('//*[@id="brdcrm_holder"]/ul/li[2]/a').click()
time.sleep(6)
#profile icon click
browser.find_element_by_xpath('//*[@id="header-II"]/section/nav/div/ul[2]/li[1]/a/img').click()
time.sleep(2)
# for logging out
browser.find_element_by_xpath('//*[@id="header-II"]/section/nav/div/ul[2]/li[1]/ul/li[7]/a').click()

