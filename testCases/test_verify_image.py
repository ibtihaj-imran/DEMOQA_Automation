from pageObjects.Verify_image import verifyimage
from Configratins.elements import data
from cofitest import setup
import time


class Test_003_VerifyImage:
    baseURL = data.baseURL

    def test_verifyimage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.vi = verifyimage(self.driver)
        self.driver.maximize_window()
        self.vi.clickElements()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.vi.clickBrokenLinksImg()
        time.sleep(5)
        self.driver.close()
