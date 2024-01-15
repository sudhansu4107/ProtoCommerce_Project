from Pom.Home_page import Home
from Utilities.Base_class import Baseclass


class Test_Home(Baseclass):

    def test_register(self):
        home = Home(self.driver)
        home.fill_name()
        home.fill_Email()
        home.fill_password()
        home.Do_you_like_Icecreams()
        home.Select_gender()
        home.Select_employment_status()
        home.Select_dob()
        home.click_submit()
        home.success_message()
        home.close_msg()


