import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test_facebook:

    def test_login(self):

        self.driver.get("https://en-gb.facebook.com/")
        username = self.driver.find_element_by_id("email")
        username.send_keys("kumar.sathish189@gmail.com")
        paswword = self.driver.find_element_by_css_selector("input[data-testid=royal_pass]")
        paswword.send_keys("Admin@123")
        # driver.find_element_by_xpath("//button[contains(@id,'u_0_')]").click()
        self.driver.find_element_by_xpath("//button[starts-with(@id,'u_0_')]").click()

    def test_logout(self):

        time.sleep(3)

        self.driver.find_element_by_xpath("(//div[@aria-label='Account'])[1]").click()
        time.sleep(3)
        #WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(By.XPATH, "(//span[text()='Log Out']//parent::div)[1]"))
        self.driver.find_element(By.XPATH,"(//span[text()='Log Out']//parent::div)[1]").click()