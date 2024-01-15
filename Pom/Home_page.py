from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Utilities.Base_class import Baseclass
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Home(Baseclass):
    Name = "(//input[@name='name'])[1]"
    Email = "(//input[@name='email'])[1]"
    Password = "(//input[@type='password'])[1]"
    Love_ice_creams = "#exampleCheck1"
    Gender = "#exampleFormControlSelect1"
    Student = "#inlineRadio1"
    Employed = "#inlineRadio2"
    Entrepreneur = "#inlineRadio3"
    Dob = "(//input[@class='form-control'])[2]"
    Submit = ".btn-success"
    Data_Binding_Text_box = "(//input[@name='name'])[2]"
    Success_message = ".alert-dismissible"
    close=".close"

    def __init__(self, driver):
        self.driver = driver

    def fill_name(self):
        Name_field = self.driver.find_element(By.XPATH, Home.Name)
        Name_field.clear()
        Name_field.send_keys("Sudhansu")

    def fill_Email(self):
        Email_field = self.driver.find_element(By.XPATH, Home.Email)
        Email_field.clear()
        Email_field.send_keys("SudhansuDummy1@gmail.com")

    def fill_password(self):
        Email_field = self.driver.find_element(By.XPATH, Home.Password)
        Email_field.clear()
        Email_field.send_keys("Qwerty!")

    def Do_you_like_Icecreams(self):
        Icecreams_field = self.driver.find_element(By.CSS_SELECTOR, Home.Love_ice_creams)
        Icecreams_field.click()

    def Select_gender(self):
        Gender_selection=self.driver.find_element(By.CSS_SELECTOR,Home.Gender)
        drp=Select(Gender_selection)
        drp.select_by_visible_text("Male")

    def Select_employment_status(self):
        Select_status=self.driver.find_element(By.CSS_SELECTOR,Home.Student)
        Select_status.click()

    def Select_dob(self):
        DOB=self.driver.find_element(By.XPATH,Home.Dob)
        DOB.clear()
        DOB.send_keys("15-01-2024")

    def click_submit(self):
        Submit_btn=self.driver.find_element(By.CSS_SELECTOR,Home.Submit)
        Submit_btn.click()

    def success_message(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,Home.Success_message)))
        success_msg = self.driver.find_element(By.CSS_SELECTOR, Home.Success_message)
        # print(success_msg.text)
        if success_msg.text=="Success! The Form has been submitted successfully!.":
            print("The Registration is completed successfully.")
        else:
            print("The Registration is not  completed successfully.")

    def close_msg(self):
        cross=self.driver.find_element(By.CSS_SELECTOR,Home.close)
        cross.click()






