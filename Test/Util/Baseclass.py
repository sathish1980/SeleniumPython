import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Baseclass:
    def welementtobeclickable(self , elementvalue):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(elementvalue))

    def welementtobevisible(self , elementvalue):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(elementvalue))