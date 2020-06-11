import inspect
import json
import logging
import configparser

import pytest
from selenium import webdriver
import time


driver = None


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    global driver
    baseClass = BaseClass()
    #    browser_name=request.config.getoption("browser_name")
#    if browser_name == "chrome":
    BaseClass.driver = webdriver.Chrome(executable_path= baseClass.configfileParser("ChromeDriverPath"))
    BaseClass.driver.get(baseClass.configfileParser("URL"))
    BaseClass.driver.maximize_window()
    from pageObjects.SignInPage import SignInPage
    signIn = SignInPage(BaseClass.driver)
    signIn.click_on_button(signIn.login)
    signIn.enter_text(signIn.emailIdText, baseClass.configfileParser("LogInEmailId"))
    signIn.click_on_button(signIn.nextbutton)
    signIn.enter_text(signIn.passwordText, baseClass.configfileParser("Password"))
    signIn.click_on_button(signIn.sign)
    signIn.click_on_button(signIn.yes)
    yield
    BaseClass.driver.quit()




@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name1 = report.nodeid.replace("::", "_")+".png"
            file_name = file_name1.replace("/", "_")
            _capture_screenshot("/Users/tml/Desktop/Automation_Projects/Python_Project/PythonSelFramework/Screenshots/" + file_name)

            if file_name:
                html = '<div><img src="/PythonSelFramework/Screenshots/%s" alt="SCREENSHOT" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
     BaseClass.driver.get_screenshot_as_file(name)





class BaseClass:

    driver = None



    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def configfileParser(self, configParam):
        try:
            config = configparser.ConfigParser()
            config.sections()
            config.read(
                '/Users/tml/Desktop/Automation_Projects/Python_Project/PythonSelFramework/Config/config.ini')
            return config.get('SectionOne', configParam)
        except Exception as e:
            print("Exception :", e)

    def config(self, configParam):
        with open('/Users/tml/Desktop/Automation_Projects/Python_Project/PythonSelFramework/Config/config.json') as config_file:
            Data = json.load(config_file)
            return Data[configParam]














