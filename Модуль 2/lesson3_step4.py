from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    result = math.log(abs(12*math.sin(x)))
    return result
try:
    link = 'https://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    journey_button = browser.find_element(By.TAG_NAME, 'button')
    journey_button.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    x_value = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(x_value)
    time.sleep(1)
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result)
    time.sleep(1)
    submit_button = browser.find_element(By.TAG_NAME, 'button').click()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()