import pytest
from selenium import webdriver

from Testdata.loginandlogout_data import loginandlogout


@pytest.fixture(scope="class")
def setup(request):
    Br_name = request.config.getoption("browser_name")
    print(Br_name)
    if Br_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        #driver = webdriver.Chrome(chrome_options=chrome_options)
        driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe",options=chrome_options)
        #  driver = webdriver.Edge("D:\Software\edgedriver_win64_93\msedgedriver.exe")
        driver.maximize_window()
    elif Br_name == "edge":
        edge_options = webdriver.EdgeOptions()
       # edge_options.use_chromium = True
       # edge_options.add_argument("user-data-dir=/Users/user_name/Library/Application Support/Microsoft Edge/User Data")
        edge_options.add_argument("profile-directory=Profile 1")
        edge_options.add_argument("--disable-notifications");
        edge_options.add_experimental_option("useAutomationExtension", False)
        edge_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        driver = webdriver.Edge("D:\Software\edgedriver_win64\msedgedriver.exe",options=edge_options)
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
    #return driver


@pytest.fixture(scope="class")
def setup_old():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome("D:\Software\chromedriver_win32\chromedriver.exe",options=chrome_options)
    #  driver = webdriver.Edge("D:\Software\edgedriver_win64_93\msedgedriver.exe")
    driver.maximize_window()
    yield
    driver.close()
    #return driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )
@pytest.fixture(params=loginandlogout.credentials_dic)
def fblign(request):
    return  request.param