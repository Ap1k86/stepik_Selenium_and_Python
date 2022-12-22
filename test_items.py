from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# button search class
class TestFinalLesson3:

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_add_to_cart_button_search(self, browser):
        # open site
        browser.get(self.link)

        # find button. 1st way!           ↓ This 'S' is very important for assert to work.
        find_button = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        assert find_button, "!!! No 'Add to basket' buttons !!!"
        sleep(30)

        # find button. 2nd way.
        # try:
        #     browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        # except NoSuchElementException:
        #     print("\nNo add to cart button")
        # print("\nThere is an add to cart button")

# pytest --language=es test_items.py
