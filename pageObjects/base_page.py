from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def tap_on_element(self, value, selector=By.CSS_SELECTOR):
        return self.driver.find_element(selector, value).click()

    def send_key(self, value, selector=By.CSS_SELECTOR):
        return self.driver.find_element(selector, value)
