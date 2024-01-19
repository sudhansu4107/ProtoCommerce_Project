import pytest


class Test_pack2:
    def test_file3(self):
        print("This  is  the 3rd test.")

    @pytest.mark.Smoke
    def test_login(self):
        print("This is the test for  login.")

    @pytest.mark.Smoke
    def test_logout(self):
        print("This is  the test for logout.")

    @pytest.mark.skip
    def test_forget_user(self):
        print("Test for forgotten username.")

    @pytest.mark.xfail
    def test_forget_password(self):
        print("Test for forgotten password.")

