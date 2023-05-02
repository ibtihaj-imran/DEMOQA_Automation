from pageObjects.Verify_Progressbar import progressbar
from Configratins.elements import data
from cofitest import setup
import time


class Test_005_VerifyProgressBar:
    baseURL = data.baseURL

    def test_verifyprogressbar(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.vp = progressbar(self.driver)
        self.driver.maximize_window()
        self.vp.clickWidget()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.vp.clickProgressBar()
        time.sleep(2)
        self.vp.clickStartButton()
        time.sleep(13)
        self.driver.close()
