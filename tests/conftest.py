import pytest
from selenium import webdriver
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/denniswu/Desktop/Development/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/denniswu/Desktop/Development/geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://google.com")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
