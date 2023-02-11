from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('/Users/jessicamenashe/Desktop/automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

#amazon logo
driver.find_element(By.XPATH, "//input[@aria-label'Amazon']")

#continue button
driver.find_element(By.ID, 'continue')

#need help link
driver.find_element(By.XPATH, "//class[@span='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#other issues with signin link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

#conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")

#privacy of notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")



from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('/Users/jessicamenashe/Desktop/automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//h2[text()='& Orders']").click()

expected_result = driver.find_element(By.XPATH, "//input[@h1='a-spacing-small']")
actual_result = driver.find_element(By.XPATH, "//input[@h1='a-spacing-small']")
print (actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')