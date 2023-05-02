import time
from pageObjects.Verify_form import submitform
from Configratins.elements import data
from cofitest import setup
from selenium.webdriver.common.keys import Keys


class Test_004_SubmitForm:
    baseURL = data.baseURL
    Image = data.Image

    def test_submitform(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sf = submitform(self.driver)
        self.driver.maximize_window()
        self.sf.clickForms()
        self.sf.clickPractiseForm()
        self.sf.setFirstName("Gerimedica")
        self.sf.setLastName("BV")
        self.sf.setEmail("test@test.com")
        self.sf.clickGender()
        self.sf.setMobile("0123456789")
        self.sf.clickDateofBirth()
        self.sf.setYearSelect("1990")
        self.sf.setMonthSelect("January")
        self.sf.clickDateSelect()
        self.sf.setSubject("Cypress Assignment")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.sf.clickHobbies()
        self.sf.setImage(self.Image)
        self.sf.setCurrentAddress("Netherlands")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.sf.clickState()
        self.sf.Selectstate("NCR")
        self.sf.Selectstate(Keys.ENTER)
        self.sf.clickCity()
        self.sf.SelectCity("Delhi")
        self.sf.SelectCity(Keys.ENTER)
        time.sleep(2)
        self.sf.clickInteraction()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.sf.clickSubmit()
        time.sleep(5)
        self.driver.close()
