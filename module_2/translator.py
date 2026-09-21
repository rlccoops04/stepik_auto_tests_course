from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

try:
    input_value = input('Введите слово для перевода: ')
    link = 'https://translate.yandex.ru/'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(3)
    fakeArea_input = browser.find_element(By.ID, 'fakeArea')
    fakeArea_input.send_keys(input_value)
    time.sleep(3)
    answer = browser.find_element(By.CSS_SELECTOR, '#dstTextField span').text
    time.sleep(3)
    print(answer)
except Exception as e:
    print(e)
finally:
    browser.quit()