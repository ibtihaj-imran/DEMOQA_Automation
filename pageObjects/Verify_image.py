from Locators.locators import ImageLocators
from pageObjects.base_page import BasePage


class verifyimage(BasePage):

    def clickElements(self):
        return self.tap_on_element(value=ImageLocators.Element)

    def clickBrokenLinksImg(self):
        return self.tap_on_element(value=ImageLocators.BrokenLinksImg)