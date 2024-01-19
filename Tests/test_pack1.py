import pytest


@pytest.mark.usefixtures("browser")
@pytest.mark.usefixtures("data_load")
class Test_pack1:

    def test_m1(self, data_load):
        print("m1 method")
        # for i in data_load:
        #     print(i)

    def test_m2(self):
        print("this is m2 method.")

    @pytest.mark.usefixtures("cross_browser")
    def test_m3(self, cross_browser):
        print(cross_browser)
