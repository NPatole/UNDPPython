import time
import pytest as pytest
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from tests.conftest import BaseClass, driver
from pageObjects.Users import Users
from utilities import ConfigParser
import logging


class TestUsers(BaseClass):
    users = Users(driver)

    # def test_navigateToUsersMenu(self):
    #     time.sleep(5)
    #     if not TestUsers.users.element_is_visible(TestUsers.users.configActiveMenu):
    #         TestUsers.users.click_on_button(TestUsers.users.tenantDropDown)
    #         TestUsers.users.select_dropdown_text(TestUsers.users.teanantList, self.configfileParser("Tenant"))
    #         TestUsers.users.click_on_button(TestUsers.users.configMenu)
    #
    # def test_crud_superAdmin(self):
    #     time.sleep(2)
    #     TestUsers.users.click_on_button(TestUsers.users.usersMenu)
    #     TestUsers.users.click_on_button(TestUsers.users.superAdminTab)
    #     TestUsers.users.click_on_button(TestUsers.users.addSuperAdminButton)
    #     TestUsers.users.enter_text(TestUsers.users.nameText, self.configfileParser("UserName"))
    #     TestUsers.users.enter_text(TestUsers.users.emailIDText, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.addButton)
    #     TestUsers.users.enter_text(TestUsers.users.searchTextBox, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.deleteIcon)
    #     TestUsers.users.click_on_button(TestUsers.users.deleteButton)
    #     assert (TestUsers.users.get_text(TestUsers.users.alertDialog) == "User - prashant.tambe@undp.org has been deleted successfully.")
    #
    # def test_crud_fleetOnwer(self):
    #     time.sleep(5)
    #     TestUsers.users.click_on_button(TestUsers.users.usersMenu)
    #     TestUsers.users.click_on_button(TestUsers.users.fleetOwnerTab)
    #     TestUsers.users.click_on_button(TestUsers.users.addFleetAdminButton)
    #     TestUsers.users.enter_text(TestUsers.users.nameText, self.configfileParser("UserName"))
    #     TestUsers.users.enter_text(TestUsers.users.emailIDText, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.addButton)
    #     TestUsers.users.enter_text(TestUsers.users.searchTextBox, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.deleteIcon)
    #     TestUsers.users.click_on_button(TestUsers.users.deleteButton)
    #     assert (TestUsers.users.get_text(TestUsers.users.alertDialog) == "User - prashant.tambe@undp.org has been deleted successfully.")
    #
    # def test_crud_driver(self):
    #     time.sleep(5)
    #     TestUsers.users.click_on_button(TestUsers.users.usersMenu)
    #     TestUsers.users.click_on_button(TestUsers.users.driverTab)
    #     TestUsers.users.click_on_button(TestUsers.users.addDriverButton)
    #     TestUsers.users.enter_text(TestUsers.users.nameText, self.configfileParser("UserName"))
    #     TestUsers.users.enter_text(TestUsers.users.emailIDText, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.addButton)
    #     TestUsers.users.enter_text(TestUsers.users.searchTextBox, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.deleteIcon)
    #     TestUsers.users.click_on_button(TestUsers.users.deleteButton)
    #     assert (TestUsers.users.get_text(TestUsers.users.alertDialog) == "User - prashant.tambe@undp.org has been deleted successfully.")
    #
    #
    # def test_crud_passenger(self):
    #     time.sleep(5)
    #     TestUsers.users.click_on_button(TestUsers.users.usersMenu)
    #     TestUsers.users.click_on_button(TestUsers.users.passengerTab)
    #     TestUsers.users.click_on_button(TestUsers.users.addPassengerButton)
    #     TestUsers.users.enter_text(TestUsers.users.nameText, self.configfileParser("UserName"))
    #     TestUsers.users.enter_text(TestUsers.users.emailIDText, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.addButton)
    #     TestUsers.users.enter_text(TestUsers.users.searchTextBox, self.configfileParser("EmailId"))
    #     TestUsers.users.click_on_button(TestUsers.users.deleteIcon)
    #     TestUsers.users.click_on_button(TestUsers.users.deleteButton)
    #     assert (TestUsers.users.get_text(TestUsers.users.alertDialog) == "User - prashant.tambe@undp.org has been deleted successfully.")
    #











