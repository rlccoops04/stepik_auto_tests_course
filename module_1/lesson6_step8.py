from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys('Bulat')

    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Zigangirov')

    input3 = browser.find_element(By.CSS_SELECTOR, '.city')
    input3.send_keys('Kazan')

    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Russia')

    btn = browser.find_element(By.XPATH, '//button[text() ="Submit"]')
    btn.click()
except Exception as error:
    print(error)
finally:
    time.sleep(5)
    browser.close()
    browser.quit()