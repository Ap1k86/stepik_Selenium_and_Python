from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find sum elements.
    find_sum_1 = browser.find_element(By.ID, "num1").text
    find_sum_2 = browser.find_element(By.ID, "num2").text

    # Choose from the dropdown
    choose = Select(browser.find_element(By.TAG_NAME, 'select'))
    choose.select_by_visible_text(str(int(find_sum_1) + int(find_sum_2)))

    # click button.
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(25)

    # close the browser
    browser.quit()
