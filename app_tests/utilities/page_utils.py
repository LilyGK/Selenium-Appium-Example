from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageUtils:

    def __init__(self, driver):
        self.driver = driver

    def click_class_index(self, locator, index):
        element = WebDriverWait(self.driver, 30).until(
            ec.presence_of_all_elements_located((AppiumBy.CLASS_NAME, locator)))
        element[index].click()

    def write_class_index(self, locator, text, index):
        element = WebDriverWait(self.driver, 30).until(
            ec.presence_of_all_elements_located((AppiumBy.CLASS_NAME, locator)))
        element[index].send_keys(text)

    def check_text(self, locator):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        locator_text = element.text
        return locator_text
