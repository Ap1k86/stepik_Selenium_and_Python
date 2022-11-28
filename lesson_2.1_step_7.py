import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# import from a separate file
from calc import calc


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find image.
    find_image = browser.find_element(By.ID, "treasure").get_attribute("valuex")

    # input valuex.
    input_valuex = browser.find_element(By.ID, "answer")
    input_valuex.send_keys(calc(find_image))

    # click checkbox.
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # click radio.
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    # click button.
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(15)

    # close the  browser
    browser.quit()
