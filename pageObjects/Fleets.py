from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from tests.conftest import BaseClass


class Fleets(BasePage):
    baseClass = BaseClass()

    def __init__(self, driver):
        BasePage.driver = driver

    tenantDropDown = (By.XPATH, "//span[@class='ng-arrow-wrapper']//preceding :: span[@class='ng-arrow-wrapper']")
    teanantList = (By.XPATH, "//div[@role='option']")
    configMenu = (By.XPATH, "//span[text()='Configuration']")
    fleetsMenu = (By.XPATH, "//span[text()='Fleets']")
    addFleetButton = (By.XPATH, "//button[text()=' Add Fleet ']")
    fleetName = (By.ID, "name")
    selectMetric = (By.XPATH, "//span[@class='ng-arrow-wrapper']//following :: span[@class='ng-arrow-wrapper'][2]")
    assignOwner = (By.XPATH, "//small[text()='Assign Owner']")
    ownerListTableId = (By.XPATH, "//table[@id='ownerListTblId']")
    selectCheckBox = (By.XPATH, "//td[@class='no-sort']")
    assignButton = (By.XPATH, "//button[text()='Assign']")
    cancelButton = (By.XPATH, "//button[text()='Cancel']")
    addButton = (By.XPATH, "//button[text()='Add']")
    deleteFleetIcon = (By.XPATH, "//a[@title='Delete Fleet']")
    deleteButton = (By.XPATH, "//button[text()='Delete']")

    def assignOwnerToFleet(self):
        self.click_on_button(self.assignOwner)
        self.enter_text(self.searchTextBox, Fleets.baseClass.configfileParser("UserName"))
        self.click_on_button(self.selectCheckBox)
        self.click_on_button(self.assignButton)
        self.click_on_button(self.addButton)

    def addFleet(self):
        self.click_on_button(self.addFleetButton)
        self.enter_text(self.fleetName, Fleets.baseClass.configfileParser("FleetName"))
        self.assignOwnerToFleet()

    def deleteFleet(self):
        self.click_on_button(self.deleteFleetIcon)
        self.click_on_button(self.deleteButton)
