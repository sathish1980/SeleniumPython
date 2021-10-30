from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Test.Util.Baseclass import Baseclass


class logout_page:
    logout_dr = (By.XPATH,"(//div[@aria-label='Account'])[1]")
    logout_btn = (By.XPATH,"(//span[text()='Log Out']//parent::div)[1]")

    def __init__(self,driver):
        self.driver = driver
    def logoutdropdown(self):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.driver.find_element(*logout_page.logout_dr)))
        return self.driver.find_element(*logout_page.logout_dr)
    def logoutbutton(self):
       #WebDriverWait(self.driver, 60).until(
        #    EC.element_to_be_clickable(self.driver.find_element(*logout_page.logout_btn)))
        #Baseclass.welementtobeclickable(self.driver.find_element(*logout_page.logout_btn))
        lgbutton = self.driver.find_element(*logout_page.logout_btn)
        return lgbutton
