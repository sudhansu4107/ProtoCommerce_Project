import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup(request):
    ser_obj = Service("../Webdrivers/chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.cls.driver=driver

