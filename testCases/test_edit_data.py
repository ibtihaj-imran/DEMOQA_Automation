from pageObjects.Edit_data import editdata
from Configratins.elements import data
from cofitest import setup


class Test_002_EditData:
    baseURL = data.baseURL

    def test_editdata(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.ed = editdata(self.driver)
        self.driver.maximize_window()
        self.ed.clickElements()
        self.ed.clickWebTables()
        self.ed.clickEditButton()
        self.ed.setFirstName("Gerimedica")
        self.ed.setLastName("BV")
        self.ed.clickSubmit()
        self.driver.close()
