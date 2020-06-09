import time

from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage
from tests.conftest import BaseClass


class Users(BasePage):

    def __init__(self, driver):
        BasePage.driver = driver

    tenantDropDown = (By.XPATH, "//ng-select[@id ='selectTenant']")
    teanantList = (By.XPATH, "//div[@role='option']")
    configMenu = (By.XPATH, "//span[text()='Configuration']")
    usersMenu = (By.XPATH, "//span[text()='Users']")
    superAdminTab = (By.ID, "superAdminTab")
    addSuperAdminButton = (By.XPATH, "//button[text()=' Add Super Admin ']")
    fleetOwnerTab = (By.ID, "fleetOwnerTab")
    addFleetAdminButton = (By.XPATH, "//button[text()=' Add Fleet Owner ']")
    driverTab = (By.ID, "driverTab")
    addDriverButton = (By.XPATH, "//button[text()=' Add Driver ']")
    passengerTab = (By.ID, "passengerTab")
    addPassengerButton = (By.XPATH, "//button[text()=' Add Passenger ']")
#    searchTextBox = (By.XPATH, "//input[@type='search']")
#    tableId = (By.XPATH, "//table[@id='userDatatableId']")
    nameText = (By.XPATH, "//input[@id ='inputName']")
    emailIDText = (By.XPATH, "//input[@id ='inputEmail']")
    addButton = (By.XPATH, "//button[text()='Add']")
    deleteIcon =(By.XPATH, "//i[@class ='far fa-trash-alt text-danger']")
    deleteButton = (By.XPATH, "//button[@class='btn btn-outline-dark app-btn']")
    alertDialog = (By.XPATH, "//div[@role='alertdialog']")



    def addFleetOwner(self):
        baseClass = BaseClass()
        self.click_on_button(self.usersMenu)
        self.click_on_button(self.fleetOwnerTab)
        self.click_on_button(self.addFleetAdminButton)
        self.enter_text(self.nameText, baseClass.configfileParser("UserName"))
        self.enter_text(self.emailIDText, baseClass.configfileParser("EmailId"))
        self.click_on_button(self.addButton)
