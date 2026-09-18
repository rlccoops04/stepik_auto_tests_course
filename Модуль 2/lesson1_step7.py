from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'treasure')
    x_value = x.get_attribute('valuex')
    y = calc(x_value)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    robot_checkbox.click()

    robot_radiobtn = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    robot_radiobtn.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_btn.click()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.close()
    browser.quit()
