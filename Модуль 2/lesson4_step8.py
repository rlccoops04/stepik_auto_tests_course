from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
    result = math.log(abs(12*math.sin(x)))
    return result

try:
    link = 'https://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book_button = browser.find_element(By.ID, 'book').click()

    x_value = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(x_value)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()
