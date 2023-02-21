from selenium.webdriver.common.by import By

service = Service('/chromedriver')
driver = webdriver.Chrome(service=service)

#Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#Your name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Mobile or email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#password
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#reenter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#continue
driver.find_element(By.CSS_SELECTOR, '#continue')

#privacy notice
driver.find_element(By.CSS_SELECTOR, '#a[href*="ap register_notification_privacy_notice"]')

#conditions of use
driver.find_element(By.CSS_SELECTOR, '#a[href*="ap_register_notification_privacy_notice"]' )
