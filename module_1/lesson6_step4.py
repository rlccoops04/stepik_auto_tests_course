from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/simple_form_find_task.html')
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys('Bulat')

    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Zigangirov')

    input3 = browser.find_element(By.CSS_SELECTOR, '.city')
    input3.send_keys('Kazan')

    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Russia')

    btn = browser.find_element(By.ID, 'submit_button')
    btn.click()
finally:
    browser.close()
    time.sleep(2)
    browser.quit()