from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from calc import calc

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # click button 1.
    click_button_1 = browser.find_element(By.TAG_NAME, "button")
    click_button_1.click()

    # click alert.
    click_alert = browser.switch_to.alert
    click_alert.accept()

    # read x.
    read_x = browser.find_element(By.ID, "input_value").text

    # input x.
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(calc(read_x))

    # click submit 2.
    click_button_2 = browser.find_element(By.TAG_NAME, "button")
    click_button_2.click()

    # read alert!
    read_alert = browser.switch_to.alert.text
    good_text = read_alert.split(': ')[-1]
    print(f"Введенный текст: {good_text}")

finally:
    sleep(5)

    # quit browser
    browser.quit()
