from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')

    firstname_input = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    firstname_input.send_keys('Bulat')

    lastname_input = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lastname_input.send_keys("Zigangirov")

    email_input = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email_input.send_keys("email@email.com")

    file_input = browser.find_element(By.ID, "file")
    file_path = os.path.join(os.path.dirname(__file__), "test.txt")
    file_input.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()
    browser.find_element_by_tag_name()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()