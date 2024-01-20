import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(

        "--browser_name", action="store", default="chrome"

    )


@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("browser_name")
    global driver
    global ser_obj
    if browser == "chrome":
        ser_obj = Service("G:\\ProtoCommerce_Project\\Webdrivers\\chromedriver.exe")
        option = Options()
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        option.add_argument('--ignore--certificate-errors')
        driver = webdriver.Chrome(service=ser_obj,options=option)
        print("Chrome  browser is triggered.")
    elif browser == "edge":
        ser_obj = Service("G:\\ProtoCommerce_Project\\Webdrivers\\msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj)
        print("Edge is triggered")
    elif browser == "gecko":
        ser_obj = Service("G:\\ProtoCommerce_Project\\Webdrivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj)
        print("gecko browser is  triggered.")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.cls.driver = driver


@pytest.fixture(scope='class')
def browser():
    print("Login to the browser.")
    yield
    print("Logout from the browser.")


# Data load fixture
@pytest.fixture
def data_load():
    return ["sudhansu", "27", "32000"]


@pytest.fixture(params=["sudhansu", "27", "32000"])
def cross_browser(request):
    return request.param
