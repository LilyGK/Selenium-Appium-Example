from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WebPageUtils:

    def __init__(self, driver):
        self.driver = driver

    def open_web(self, url):
        self.driver.get(url)

    def click_xpath(self, locator):
        element = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, locator)))
        element.click()

    def write_xpath(self, locator, text):
        element = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, locator)))
        element.send_keys(text)

    def check_text(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        locator_text = element.text
        return locator_text
