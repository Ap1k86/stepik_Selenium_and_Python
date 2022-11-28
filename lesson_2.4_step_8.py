from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from time import sleep
from calc import calc

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find price.
    print("find price.")
    WebDriverWait(browser, 15).until(es.text_to_be_present_in_element((By.ID, "price"), "100"))

    # click button 1.
    print("click button 1.")
    click_button_1 = browser.find_element(By.ID, "book")
    click_button_1.click()

    # scroll down after click.
    print("scroll down after click.")
    click_button_2 = browser.find_element(By.ID, "solve")
    scroll_down = browser.execute_script("return arguments[0].scrollIntoView(true);", click_button_2)

    # find input x.
    print("find input x.")
    find_input_x = browser.find_element(By.ID, "input_value").text

    # input x.
    print("input x.")
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(calc(find_input_x))

    # click button 2.
    print("click button 2.")
    click_button_2 = browser.find_element(By.ID, "solve")
    click_button_2.click()

    # read alert.
    print("FINE!")
    read_alert = browser.switch_to.alert.text
    print(f'\nMy code is: {read_alert.split(": ")[-1]}')

finally:
    sleep(30)

    # quit browser
    browser.quit()
