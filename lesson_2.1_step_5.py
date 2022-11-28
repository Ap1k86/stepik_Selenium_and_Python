from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
k = 225


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x_number)))))


try:
    link = "https://suninjuly.github.io/math.html"

    # open browser.
    browser = webdriver.Chrome()
    browser.get(link)

    # Find element x.
    x_element = browser.find_element(By.ID, "input_value")
    x_number = x_element.text
    y = calc(x_number)

    # Find input field
    find_input = browser.find_element(By.ID, "answer")
    find_input.send_keys(y)

    # click the first element. !Work.
    click_checkbox = browser.find_element(By.XPATH,
                                          "//div[@class='form-check form-check-custom']"
                                          "//input[@class='form-check-input']")
    click_checkbox.click()

    # click the second element.
    click_radio = browser.find_element(By.ID, "robotsRule")
    click_radio.click()

    # press the button. !Work.
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)

    # close the browser.
    browser.quit()
