from Locators.locators import TooltipLocators
from pageObjects.base_page import BasePage


class tooltips(BasePage):

    def clickWidget(self):
        return self.tap_on_element(value=TooltipLocators.Widget)

    def clickToolTIps(self):
        return self.tap_on_element(value=TooltipLocators.ToolTips)

    def clickMoveButton(self):
        return self.tap_on_element(value=TooltipLocators.MoveButton)