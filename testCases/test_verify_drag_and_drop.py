import time

from pageObjects.Verify_drag_and_drop import DragandDrop
from Configratins.elements import data
from cofitest import setup
from selenium.webdriver import ActionChains


class Test_007_Verifydraganddrop:
    baseURL = data.baseURL

    def test_verifdraganddrop(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.dd = DragandDrop(self.driver)
        self.driver.maximize_window()
        self.dd.clickInteraction()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.dd.clickDroppable()
        time.sleep(2)
        elm1 = self.dd.DragBox()
        self.dd.DRopArea()
        ActionChains(self.driver).drag_and_drop_by_offset(elm1, 269, 54)
        self.driver.close()
