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

driver.quit()

