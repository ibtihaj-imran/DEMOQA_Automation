from pageObjects.Verify_Tooltip import tooltips
from Configratins.elements import data
from cofitest import setup
import time


class Test_006_Verifytooltips:
    baseURL = data.baseURL

    def test_verifytooltips(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.vt = tooltips(self.driver)
        self.driver.maximize_window()
        self.vt.clickWidget()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.vt.clickToolTIps()
        time.sleep(3)
        self.vt.clickMoveButton()
        time.sleep(3)
        self.driver.close()
