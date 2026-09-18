from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    result = math.log(abs(12*math.sin(x)))
    return result
try:
    link = 'https://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    journey_button = browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x_value = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(x_value)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result)
    time.sleep(1)
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()
