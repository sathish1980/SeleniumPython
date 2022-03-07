from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonActions:

    def explictiwaitbyName(self,nameAttribute):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.NAME, nameAttribute)))
    def explictiwaitbyXpath(self,xpathAttribute):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.Xpath, xpathAttribute)))
    def explictiwaitbyNameforclickable(self,nameAttribute):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, nameAttribute)))
    def explictiwaitbyxpathforclickable(self, xpathAttribute):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, xpathAttribute)))

    def textBoxvaluebyName(self,TextboxElement,TexttobeEnter):
        self.TextboxElement.clear()
        self.TextboxElement.send_keys(TexttobeEnter)
