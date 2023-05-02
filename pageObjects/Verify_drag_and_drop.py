from Locators.locators import DraganddropLocators
from pageObjects.base_page import BasePage


class DragandDrop(BasePage):

    def clickInteraction(self):
        return self.tap_on_element(value=DraganddropLocators.Interactions)

    def clickDroppable(self):
        return self.tap_on_element(value=DraganddropLocators.Droppable)

    def clickMoveButton(self):
        return self.tap_on_element(value=DraganddropLocators.MoveButton)

    def DragBox(self):
        self.driver.find_element(*DraganddropLocators.DragBox)

    def DRopArea(self):
        self.driver.find_element(*DraganddropLocators.DropArea)
