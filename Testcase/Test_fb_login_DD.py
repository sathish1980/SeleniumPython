import time

import pytest

from Pages.Login_page  import login_page
from Pages.Logout_page import logout_page
from Test.Util.Baseclass import Baseclass
from Testdata.loginandlogout_data import loginandlogout


class Test_fbloginDD(Baseclass):

    def loginDD(self,fbloign):
        self.driver.get("https://en-gb.facebook.com/")
        lp = login_page(self.driver)
        #print("done")
       # lp.username().send_keys(fbloign[0])
       # lp.password().send_keys(fbloign[1])
        lp.username(fbloign["username"])
        lp.password().send_keys(fbloign["password"])
        lp.login_button().click()
        lp = logout_page(self.driver)
        self.welementtobeclickable( lp.logoutdropdown())
        lp.logoutdropdown().click()
        time.sleep(2)
        self.welementtobeclickable(lp.logoutbutton())
        lp.logoutbutton().click()

    def test_loginDDwithexcel(self,fbloign):

        #print("done")
       # lp.username().send_keys(fbloign[0])
       # lp.password().send_keys(fbloign[1])
        size=len(loginandlogout.credential_excel_dic[0])
        print(size)
        value = size/2
        print(int(value))
        for i in range(1,int(value)+1) :
            self.driver.get("https://en-gb.facebook.com/")
            lp = login_page(self.driver)
            lp.username(fbloign["username"+str(i)])
            lp.password().clear()
            lp.password().send_keys(fbloign["password"+str(i)])
            lp.login_button().click()
            lp = logout_page(self.driver)
            self.welementtobeclickable( lp.logoutdropdown())
            lp.logoutdropdown().click()
            time.sleep(2)
            self.welementtobeclickable(lp.logoutbutton())
            lp.logoutbutton().click()

    #@pytest.fixture(params=[("kumar.sathish189@gmail.com","Admin@123"), ("kumar.sathish189@gmail.com","Admin@123")])
    #@pytest.fixture(params=loginandlogout.credentials)
    #@pytest.fixture(params=loginandlogout.credentials_dic)
    @pytest.fixture(params=loginandlogout.credential_excel_dic)
    def fbloign(self,request):
        return  request.param

