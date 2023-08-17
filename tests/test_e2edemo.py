import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from Utilities.BaseClass import BaseClass
from PageObject.SearchHKO import SearchHKO


class TestSearchHKO(BaseClass):

    def test_e2edemo(self):

        google = SearchHKO(self.driver)
        search_bar_element = google.search_bar()
        search_bar_element.send_keys("香港天文台")
        search_bar_element.send_keys(Keys.RETURN)
        google.clickResult().click()

        Mintemp = google.getMinTemp()
        MinNum = Mintemp.text

        Maxtemp = google.getMaxTemp()
        MaxNum = Maxtemp.text

        try:
            assert Mintemp.is_displayed() and Maxtemp.is_displayed()
            print(f"Current Maximum and Minimum temperature {MaxNum} & {MinNum} are displayed")
        except AssertionError:
            if not Mintemp.is_displayed():
                print("Minimum temperature is not displayed")
            if not Maxtemp.is_displayed():
                print("Maximum temperature is not displayed")

        self.take_screenshot("xxx.png")



        time.sleep(2)