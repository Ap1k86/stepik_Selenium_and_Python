from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill input
    print("fill input")
    fill_input = browser.find_elements(By.XPATH, "//input[@class='form-control']")
    for element in fill_input:
        element.send_keys("some text")

    # download file
    print("download file")
    download_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'f.txt')  # добавляем к этому пути имя файла
    download_file.send_keys(file_path)

    # click button
    print("click button")
    click_button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", click_button)
    click_button.click()

finally:
    sleep(30)
    # quit browser
    browser.quit()
