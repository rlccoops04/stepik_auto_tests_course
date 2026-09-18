from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

try: 
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/find_link_text')

    link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys('Bulat')

    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Zigangirov')

    input3 = browser.find_element(By.CSS_SELECTOR, '.city')
    input3.send_keys('Kazan')

    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Russia')

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()
finally:
    time.sleep(5)
    browser.close()
    browser.quit()
