from Locators.locators import DataenterLocators
from pageObjects.base_page import BasePage


class dataenter(BasePage):

    def clickElements(self):
        return self.tap_on_element(value=DataenterLocators.Elemnet)

    def clickWebTables(self):
        return self.tap_on_element(value=DataenterLocators.WebTables)

    def clickAddbutton(self):
        return self.tap_on_element(value=DataenterLocators.Addbutton)

    def setFirstName(self, FirstName):
        return self.send_key(value=DataenterLocators.FirstName).send_keys(FirstName)

    def setLastName(self, LastName):
        return self.send_key(value=DataenterLocators.LastName).send_keys(LastName)

    def setEmail(self, Email):
        return self.send_key(value=DataenterLocators.Email).send_keys(Email)

    def setAge(self, Age):
        return self.send_key(value=DataenterLocators.Age).send_keys(Age)

    def setSalary(self, Salary):
        return self.send_key(value=DataenterLocators.Salary).send_keys(Salary)

    def setDepartment(self, Department):
        return self.send_key(value=DataenterLocators.Department).send_keys(Department)

    def clickSubmit(self):
        return self.tap_on_element(value=DataenterLocators.Submit)
