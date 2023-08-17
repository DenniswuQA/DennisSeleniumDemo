import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.BaseClass import BaseClass
from PageObject.SearchHKO import SearchHKO


class TestSearchHKO(BaseClass):

    def test_e2edemo(self):

        google = SearchHKO(self.driver)
        search_bar_element = google.search_bar()
        search_bar_element.send_keys("香港天文台")
        search_bar_element.send_keys(Keys.RETURN)
        google.clickResult().click()
        google.getHotwarning().click()

        self.take_screenshot("xxx.png")



        time.sleep(5)