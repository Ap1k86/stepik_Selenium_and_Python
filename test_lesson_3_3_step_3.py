from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_site1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля.
    # Заполняем имя.
    input_name = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']//input[@class='form-control first']")
    input_name.send_keys("Vitali")

    # Заполняем фамилию.
    input_last_name = browser.find_element(By.XPATH,
                                           "//div[@class='first_block']//input[@class='form-control "
                                           "second']")
    input_last_name.send_keys("Mitor")

    # Заполняем email.
    input_email = browser.find_element(By.XPATH,
                                       "//div[@class='first_block']//input[@class='form-control third']")
    input_email.send_keys("123@mail.ru")

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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # закрываем браузер после всех манипуляций
    browser.quit()


def test_site2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля.
    # Заполняем имя.
    input_name = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']//input[@class='form-control first']")
    input_name.send_keys("Vitali")

    # Заполняем фамилию.
    input_last_name = browser.find_element(By.XPATH, "//div[@class='first_block']//input["
                                                     "@class='form-control second']")
    input_last_name.send_keys("Mitor")

    # Заполняем email.
    input_email = browser.find_element(By.XPATH,
                                       "//div[@class='first_block']//input[@class='form-control third']")
    input_email.send_keys("123@mail.ru")

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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # закрываем браузер после всех манипуляций
    browser.quit()


if __name__ == "__main__":
    pytest.main()

"""                                         second:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class TestPyT:

    def test_site1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля.
            # Заполняем имя.
            input_name = browser.find_element(By.XPATH,
                                              "//div[@class='first_block']//input[@class='form-control first']")
            input_name.send_keys("Vitali")

            # Заполняем фамилию.
            input_last_name = browser.find_element(By.XPATH,
                                                   "//div[@class='first_block']//input[@class='form-control "
                                                   "second']")
            input_last_name.send_keys("Mitor")

            # Заполняем email.
            input_email = browser.find_element(By.XPATH,
                                               "//div[@class='first_block']//input[@class='form-control third']")
            input_email.send_keys("123@mail.ru")

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

        finally:
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text

            # закрываем браузер после всех манипуляций
            browser.quit()

        assert "Congratulations! You have successfully registered!" == welcome_text, "first test failed"

    def test_site2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля.
            # Заполняем имя.
            input_name = browser.find_element(By.XPATH,
                                              "//div[@class='first_block']//input[@class='form-control first']")
            input_name.send_keys("Vitali")

            # Заполняем фамилию.
            input_last_name = browser.find_element(By.XPATH, "//div[@class='first_block']//input["
                                                             "@class='form-control second']")
            input_last_name.send_keys("Mitor")

            # Заполняем email.
            input_email = browser.find_element(By.XPATH,
                                               "//div[@class='first_block']//input[@class='form-control third']")
            input_email.send_keys("123@mail.ru")

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

        finally:
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text

            # закрываем браузер после всех манипуляций
            browser.quit()
        assert "Congratulations! You have successfully registered!" == welcome_text, "second text failed"


if __name__ == "__main__":
    pytest.main()
"""
