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
        Mintemp = google.getTemp()

        try:
            if Mintemp.is_displayed():
                print ("Current MinTem is displayed")
            else:
                print ("HKO did not show Mintemp")
        except NoSuchElementException:
            print("Mintemp not found")

        self.take_screenshot("xxx.png")



        time.sleep(5)