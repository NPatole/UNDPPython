from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class SignInPage(BasePage):

    def __init__(self, driver):
        BasePage.driver = driver

    login = (By.XPATH, "//button[text()='Sign in']//following::button[1]")
    emailIdText = (By.XPATH, "//input[@type='email']")
    passwordText = (By.XPATH, "//input[@type='password']")
    nextbutton = (By.ID, "idSIButton9")
    sign = (By.ID, "submitButton")
    yes = (By.XPATH, "//input[@type='submit']")




    def loginButton(self):
        self.driver.find_element(*SignInPage.login)
        return self.driver.find_element(*SignInPage.login)

    def email(self):
        self.driver.find_element(*SignInPage.emailIdText)
        return self.driver.find_element(*SignInPage.emailIdText)

    def next(self):
        self.driver.find_element(*SignInPage.nextbutton)
        return self.driver.find_element(*SignInPage.nextbutton)

    def password(self):
        self.driver.find_element(*SignInPage.passwordText)
        return self.driver.find_element(*SignInPage.passwordText)

    def singnIn(self):
        self.driver.find_element(*SignInPage.sign)
        return self.driver.find_element(*SignInPage.sign)

    def yesButton(self):
        self.driver.find_element(*SignInPage.yes)
        return self.driver.find_element(*SignInPage.yes)







