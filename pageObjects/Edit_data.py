from Locators.locators import EditdataLocators
from pageObjects.base_page import BasePage


class editdata(BasePage):

    def clickElements(self):
        return self.tap_on_element(value=EditdataLocators.Element)

    def clickWebTables(self):
        return self.tap_on_element(value=EditdataLocators.WebTables)

    def clickEditButton(self):
        return self.tap_on_element(value=EditdataLocators.EditButton)

    def setFirstName(self, FirstName):
        return self.send_key(value=EditdataLocators.FirstName).send_keys(FirstName)

    def setLastName(self, LastName):
        return self.send_key(value=EditdataLocators.LastName).send_keys(LastName)

    def clickSubmit(self):
        return self.tap_on_element(value=EditdataLocators.Submit)
