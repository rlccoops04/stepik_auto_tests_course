from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    summa = int(num1.text) + int(num2.text)

    select = browser.find_element(By.XPATH, '//select[@id="dropdown"]').click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{summa}"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
except Exception as e:
    print(e)
finally:
    time.sleep(3)
    browser.quit()