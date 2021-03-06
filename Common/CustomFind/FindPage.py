from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocatorsClass():
    def __init__(self, driver):
        self.driver = driver


    def custom_find(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)
            )

            return element
        except:

            self.driver.save_screenshot("../Common/Screenshots/Screen.png")

            print("EROOR: Element not found!!")
            exit(2)

