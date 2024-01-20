import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Chromeoptions = Options()
prefs = {"download.default_directory": "G:\\ProtoCommerce_Project\\Download"}
Chromeoptions.add_experimental_option("prefs", prefs)

ser_obj = Service("G:\\ProtoCommerce_Project\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=Chromeoptions)
driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")
driver.maximize_window()
driver.implicitly_wait(10)


def test_Download():
    Static = driver.find_element(By.XPATH, "(//div/h6)[1]")
    First = driver.find_element(By.XPATH, "(//div[@class='download-csv'])[1]/a")
    wait = WebDriverWait(driver, 10)
    driver.execute_script("arguments[0].scrollIntoView();", Static)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='download-csv'])[1]")))
    print("Before downloading the file.")
    First.click()
    print("After downloading the file.")
    print("Download  Test is completed")