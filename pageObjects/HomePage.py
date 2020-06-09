from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        BasePage.driver = driver

    tenantDropDown = (By.XPATH, "//span[@class='ng-arrow-wrapper']//preceding :: span[@class='ng-arrow-wrapper']")
    teanantList = (By.XPATH, "//div[@role='option']")
    configMenu = (By.XPATH, "//span[text()='Configuration']")
    usersMenu = (By.XPATH, "//span[text()='Users']")
    addSuperAdminButton = (By.XPATH, "//button[text()=' Add Super Admin ']")
    addName = (By.ID, "inputName")
    addEmailID =(By.ID, "inputEmail")
    addMobileNumber = (By.ID, "mobileNumber")
    addButton = (By.XPATH, "//button[text()='Add']")



    def selectTenantDropDown(self):
        self.driver.find_element(*HomePage.login)
        return self.driver.find_element(*HomePage.tenantDropDown)










