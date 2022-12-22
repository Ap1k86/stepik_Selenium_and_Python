from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestConnect(unittest.TestCase):
    def test_site1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        # Ваш код, который заполняет обязательные поля.
        # Заполняем имя.
        self.input_name = self.browser.find_element(By.XPATH,
                                                    "//div[@class='first_block']//input[@class='form-control first']")
        self.input_name.send_keys("Vitali")

        # Заполняем фамилию.
        self.input_last_name = self.browser.find_element(By.XPATH,
                                                         "//div[@class='first_block']//input[@class='form-control "
                                                         "second']")
        self.input_last_name.send_keys("Mitor")

        # Заполняем email.
        self.input_email = self.browser.find_element(By.XPATH,
                                                     "//div[@class='first_block']//input[@class='form-control third']")
        self.input_email.send_keys("123@mail.ru")

        # Отправляем заполненную форму
        self.button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text)

        # закрываем браузер после всех манипуляций
        self.browser.quit()
        # self.assertEqual(, , "Should be absolute value of a number")

    def test_site2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        # Ваш код, который заполняет обязательные поля.
        # Заполняем имя.
        self.input_name = self.browser.find_element(By.XPATH,
                                                    "//div[@class='first_block']//input[@class='form-control first']")
        self.input_name.send_keys("Vitali")

        # Заполняем фамилию.
        self.input_last_name = self.browser.find_element(By.XPATH, "//div[@class='first_block']//input["
                                                                   "@class='form-control second']")
        self.input_last_name.send_keys("Mitor")

        # Заполняем email.
        self.input_email = self.browser.find_element(By.XPATH,
                                                     "//div[@class='first_block']//input[@class='form-control third']")
        self.input_email.send_keys("123@mail.ru")

        # Отправляем заполненную форму
        self.button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text)

        # закрываем браузер после всех манипуляций
        self.browser.quit()
        # self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
