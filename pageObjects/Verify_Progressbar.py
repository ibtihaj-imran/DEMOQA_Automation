from Locators.locators import ProgressbarLocators
from pageObjects.base_page import BasePage


class progressbar(BasePage):

    def clickWidget(self):
        return self.tap_on_element(value=ProgressbarLocators.Widget)

    def clickProgressBar(self):
        return self.tap_on_element(value=ProgressbarLocators.ProgressBar)

    def clickStartButton(self):
        return self.tap_on_element(value=ProgressbarLocators.StartButton)
