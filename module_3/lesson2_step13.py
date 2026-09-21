import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSelenium(unittest.TestCase):
    def test_reg1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        inp1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        inp1.send_keys('Bulat')

        inp2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        inp2.send_keys('Zigangirov')

        inp3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        inp3.send_keys('realemail@email.com')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_text, f"expected {expected_text}, got {welcome_text}")
    def test_reg2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        inp1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        inp1.send_keys('Bulat')

        inp2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        inp2.send_keys('Zigangirov')

        inp3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        inp3.send_keys('realemail@email.com')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_text, f"expected {expected_text}, got {welcome_text}")


unittest.main()