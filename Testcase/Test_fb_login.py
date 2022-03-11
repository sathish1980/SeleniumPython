import time

import pytest

from Pages.Login_page  import login_page
from Pages.Logout_page import logout_page
from Test.Util.Baseclass import Baseclass

from Testdata.loginandlogout_data import loginandlogout


class Test_fblogin(Baseclass):

    def test_login(self,fblign):
        self.driver.get("https://en-gb.facebook.com/")
        lp = login_page(self.driver)
        #print("done")
        #lp.username().send_keys(fblign[0])
        #lp.password().send_keys(fblign[1])
        #lp.username().send_keys(fblign["username"])
        lp.username(fblign["username"])
        lp.password().send_keys(fblign["password"])
        self.removefileinFolder()
        self.screenshot("usercredential"+str(self.datetime()))
        lp.login_button().click()
        ls = logout_page(self.driver)
        self.welementtobeclickable( ls.logoutdropdown())
        self.screenshot("logoutdropdowndeforeclick"+str(self.datetime()))
        ls.logoutdropdown().click()
        time.sleep(2)
        self.welementtobeclickable(ls.logoutbutton())
        ls.logoutbutton().click()
        self.screenshot("logoutbuttonclick"+str(self.datetime()))

    def test_log_invalid(self):
        self.driver.get("https://en-gb.facebook.com/")
        lp = login_page(self.driver)
        #print("done")
        lp.username("kumar.sathish189@gmail.com")
        lp.password().send_keys("Admin@12345")
        lp.login_button().click()
        time.sleep(3)
        #self.welementtobevisible(lp.incorrect_credentials())
        textvalue=lp.incorrect_credentials_text().text
        print(textvalue)




