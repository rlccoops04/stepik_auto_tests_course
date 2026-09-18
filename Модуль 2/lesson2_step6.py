from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

def calc(x):
    result = math.log(abs(12*math.sin(x)))
    return result
try:
    link = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(x_value)
    
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_radiobutton.location_once_scrolled_into_view
    robot_radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()