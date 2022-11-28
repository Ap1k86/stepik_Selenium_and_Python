from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from calc import calc

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # read x.
    read_x = browser.find_element(By.ID, "input_value").text
    print(read_x)

    # Calculate mathematical function of x.
    calculate_x = calc(read_x)

    # input calculate_x.
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(calculate_x)

    # choose robotCheckbox.
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    click_button = browser.find_element(By.TAG_NAME, "button")
    # page scroll.
    browser.execute_script("return arguments[0].scrollIntoView(true);", click_button)

    # Choose robotsRule.
    robots_rule = browser.find_element(By.XPATH, "//input[@value='robots']")
    robots_rule.click()

    # click button.
    click_button.click()

finally:
    sleep(30)
    # quit browser
    browser.quit()
