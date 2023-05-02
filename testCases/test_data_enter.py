from pageObjects.Data_enter import dataenter
from Configratins.elements import data
from cofitest import setup


class Test_001_DataEnter:
    baseURL = data.baseURL

    def test_dataenter(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.dt = dataenter(self.driver)
        self.driver.maximize_window()
        self.dt.clickElements()
        self.dt.clickWebTables()
        self.dt.clickAddbutton()
        self.dt.setFirstName("Alden")
        self.dt.setLastName("Cantrell")
        self.dt.setEmail("test@test.com")
        self.dt.setAge("30")
        self.dt.setSalary("12345")
        self.dt.setDepartment("QA")
        self.dt.clickSubmit()
        self.driver.close()
