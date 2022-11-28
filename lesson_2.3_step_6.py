from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from calc import calc

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(1)

    # click button 1.
    click_button_1 = browser.find_element(By.TAG_NAME, "button")
    click_button_1.click()

    # open new window.
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # read x.
    read_x = browser.find_element(By.ID, "input_value").text

    # input x.
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(calc(read_x))

    # click button 2.
    click_button_2 = browser.find_element(By.TAG_NAME, "button")
    click_button_2.click()

    # read answer.
    read_answer = browser.switch_to.alert.text
    print(read_answer.split(': ')[-1])

finally:
    sleep(35)

    # quit browser.
    browser.quit()
