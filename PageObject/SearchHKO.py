from selenium.webdriver.common.by import By


class SearchHKO:

    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.NAME, "q")
    HKO = (By.XPATH, "//a[@href='https://www.hko.gov.hk/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Hong Kong Observatory']")
    hotIcon = (By.XPATH, "img[alt='酷熱天氣警告']")
    mintemp = (By.XPATH, "//span[@class='hkoMinTemp']")
    maxtemp = (By.XPATH, "//span[@class='hkoMaxTemp']")
    logo = (By.XPATH, "//img[@alt='VERY HOT WEATHER WARNING']")

    def search_bar(self):
        return self.driver.find_element(*self.searchBar)

    def clickResult(self):
        return self.driver.find_element(*self.HKO)

    def getHotwarning(self):
        return self.driver.find_element(*self.logo)

    def getMinTemp(self):
        return self.driver.find_element(*self.mintemp)

    def getMaxTemp(self):
        return self.driver.find_element(*self.maxtemp)
