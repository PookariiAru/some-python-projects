from selenium.webdriver import ActionChains
from selenium import webdriver
import time

username = "test@gmail.com"
password = "test"

url = "https://www.messenger.com/login/"

driver = webdriver.Edge("/Users/insertusernamehere/Downloads/msedgedriver.exe")
driver.get(url)

#for inserting input forms
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)

#for button tag
button = driver.find_element_by_id(u"loginbutton")
ActionChains(driver).move_to_element(button).click(button).perform()
time.sleep(10)

#for div or other tags like input
#driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
#or
#driver.find_element_by_id("login").click()