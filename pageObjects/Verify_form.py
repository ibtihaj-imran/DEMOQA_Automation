from Locators.locators import FormLocators
from selenium.webdriver.support.select import Select
from pageObjects.base_page import BasePage


class submitform(BasePage):

    def clickForms(self):
        return self.tap_on_element(value=FormLocators.Forms)

    def clickPractiseForm(self):
        return self.tap_on_element(value=FormLocators.PractiseForm)

    def setFirstName(self, FirstName):
        return self.send_key(value=FormLocators.FirstName).send_keys(FirstName)

    def setLastName(self, LastName):
        return self.send_key(value=FormLocators.LastName).send_keys(LastName)

    def setEmail(self, Email):
        return self.send_key(value=FormLocators.Email).send_keys(Email)

    def clickGender(self):
        return self.tap_on_element(value=FormLocators.Gender)

    def setMobile(self, Mobile):
        return self.send_key(value=FormLocators.Mobile).send_keys(Mobile)

    def clickDateofBirth(self):
        return self.tap_on_element(value=FormLocators.DateofBirth)

    def setYearSelect(self, Year):
        drp = Select(self.driver.find_element(*FormLocators.YearSelect))
        drp.select_by_visible_text(Year)

    def setMonthSelect(self, Month):
        drp1 = Select(self.driver.find_element(*FormLocators.MonthSelect))
        drp1.select_by_visible_text(Month)

    def clickDateSelect(self):
        return self.tap_on_element(value=FormLocators.DateSelect)

    def setSubject(self, Subjects):
        return self.send_key(value=FormLocators.Subjects).send_keys(Subjects)

    def clickHobbies(self):
        return self.tap_on_element(value=FormLocators.Hobbies)

    def setImage(self, Image):
        return self.send_key(value=FormLocators.SelectImage).send_keys(Image)

    def setCurrentAddress(self, Address):
        return self.send_key(value=FormLocators.CurrentAddress).send_keys(Address)

    def clickState(self):
        return self.tap_on_element(value=FormLocators.State)

    def Selectstate(self, state):
        return self.send_key(value=FormLocators.Selectstate).send_keys(state)

    def clickCity(self):
        return self.tap_on_element(value=FormLocators.City)

    def SelectCity(self, city):
        return self.send_key(value=FormLocators.SelectCity).send_keys(city)

    def clickInteraction(self):
        return self.send_key(value=FormLocators.Interactions)

    def clickSubmit(self):
        return self.send_key(value=FormLocators.Submit)
