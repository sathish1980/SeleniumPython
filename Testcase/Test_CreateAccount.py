import time

from Pages.Create_Account_page import CreateAccount_page
from Test.Util.Baseclass import Baseclass


class Test_CreateAccount(Baseclass):

    def test_CreateAccountwithValidData(self,setup):
        self.driver.get("https://en-gb.facebook.com/")
        CA = CreateAccount_page(self.driver)
        CA.CreateAccoutnButton()
        CA.Firstname("Sathish")
        CA.Surname("Kumar")
        CA.MobileorEmail("Kumar.sathish189@gmail.com")
        CA.ReenterMobileorEmail("Kumar.sathish189@gmail.com")
        CA.Newpassword("Test124")
        CA.DOB(12,"7","2000")
        CA.Gender("FeMale")
        time.sleep(2)


