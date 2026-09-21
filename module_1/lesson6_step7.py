from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/huge_form.html')
    inputs = browser.find_elements(By.TAG_NAME, 'input')
    for input in inputs:
        input.send_keys('ответ')
    btn = browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.close()
    browser.quit()