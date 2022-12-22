import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import login, password

# answer formula.
answer = math.log(int(time.time()))


@pytest.mark.parametrize("lesson", [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
class TestForMath:
    # create a list of responses.
    responses = ''

    def test_for_1(self, browser, lesson):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)

        # click button login.
        self.click_login = WebDriverWait(browser, 15).until(es.element_to_be_clickable((By.ID, "ember33")))
        self.click_login.click()

        # enter login.
        self.click_login = browser.find_element(By.XPATH, '//input[@name="login"]')
        self.click_login.send_keys(login)

        # enter password.
        self.input_password = browser.find_element(By.XPATH, "//input[@name='password']")
        self.input_password.send_keys(password)

        # click button.
        print("\nclick button")
        self.click_button = browser.find_element(By.XPATH, "//button[@type='submit']")
        self.click_button.click()
        sleep(3)

        # find input.
        self.input_field = WebDriverWait(browser, 25).until(es.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
        self.input_field.send_keys(math.log(int(time.time())))

        # click button 2.
        self.click_button_2 = WebDriverWait(browser, 25).until(
            es.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
        self.click_button_2.click()

        # find response.
        self.response = WebDriverWait(browser, 25).until(
            es.element_to_be_clickable((By.XPATH, "//p[@class='smart-hints__hint']"))).text
        assert self.response == "Correct!", print(self.response)


if __name__ == "__main__":
    pytest.main()

# The owls are not what they seem! OvO
