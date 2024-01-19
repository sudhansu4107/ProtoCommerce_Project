import sys

import pytest

sys.path.append("G:\\ProtoCommerce_Project")
from Pom.Home_page import Home
from Utilities.Base_class import Baseclass


class Test_Home(Baseclass):
    @pytest.mark.Smoke
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

    def test_file2(self):
        print("This  is the second test.")
