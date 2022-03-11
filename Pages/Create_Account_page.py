from selenium.webdriver.common.by import By

from CommonUtils.CommonActions import CommonActions


class CreateAccount_page(CommonActions):

    def __init__(self, driver):
        self.driver = driver

    createaccountButton = (By.XPATH, "//a[text()='Create New Account']")
    fname = (By.NAME, "firstname")
    sname = (By.NAME, "lastname")
    MBorEmail = (By.NAME, "reg_email__")
    reenterEmail = (By.NAME, "reg_email_confirmation__")
    passwrd = (By.NAME, "reg_passwd__")
    daydropdown = (By.ID,"day")
    monthdropdown = (By.ID, "month")
    yeardropdown = (By.ID, "year")
    GenderselectFeMale =(By.XPATH,"(//input[@name='sex'])[1]")
    GenderselectMale = (By.XPATH, "(//input[@name='sex'])[2]")
    GenderselectOther = (By.XPATH, "(//input[@name='sex'])[3]")

    # constructor

    def CreateAccoutnButton(self):
        self.ButtonClick(self.driver.find_element(*CreateAccount_page.createaccountButton))

    def Firstname(self,TexttobeEnter):
        self.explictiwaitbyName("lastname")
        self.textBoxvaluebyName(self.driver.find_element(*CreateAccount_page.fname),TexttobeEnter)

    def Surname(self, TexttobeEnter):
        self.textBoxvaluebyName( self.driver.find_element(*CreateAccount_page.sname), TexttobeEnter)

    def MobileorEmail(self, TexttobeEnter):
        self.textBoxvaluebyName( self.driver.find_element(*CreateAccount_page.MBorEmail), TexttobeEnter)

    def ReenterMobileorEmail(self, TexttobeEnter):
        self.textBoxvaluebyName( self.driver.find_element(*CreateAccount_page.reenterEmail), TexttobeEnter)

    def Newpassword(self, TexttobeEnter):
        self.textBoxvaluebyName( self.driver.find_element(*CreateAccount_page.passwrd), TexttobeEnter)

    def DOB(self,dateindex,monthvalue,yearvalue):
        self.DropdownSelectbyIndex(self.driver.find_element(*CreateAccount_page.daydropdown), dateindex)
        self.DropdownSelectbyValue( self.driver.find_element(*CreateAccount_page.monthdropdown), monthvalue)
        self.DropdownSelectbyVisibleText(self.driver.find_element(*CreateAccount_page.yeardropdown), yearvalue)

    def Gender(self,gendertobeselect):
        if gendertobeselect=="Male":
            self.GenderSelection(self.driver.find_element(*CreateAccount_page.GenderselectMale))
        elif gendertobeselect=="FeMale":
            self.GenderSelection(self.driver.find_element(*CreateAccount_page.GenderselectFeMale))
        else:
            self.GenderSelection( self.driver.find_element(*CreateAccount_page.GenderselectOther))

