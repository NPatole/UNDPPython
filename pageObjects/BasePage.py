import time

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from tests.conftest import driver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    userTableId = (By.XPATH, "//table[@id='userDatatableId']")
    fleetTableId = (By.XPATH, "//table[@id='fleetListTblId']")
    searchTextBox = (By.XPATH, "//input[@type='search']")
    alertDialog = (By.XPATH, "//div[@role='alertdialog']")
    configActiveMenu = (By.XPATH, "//a[@aria-expanded='true' and @href='#Configuration']")

    def wait_for_element(self, locator):

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    def click_on_button(self, locator):

        try:
            time.sleep(2)
            self.wait_for_element(locator)
            self.driver.find_element(*locator).click()
        except  StaleElementReferenceException as Exception:
            time.sleep(10)
            self.wait_for_element(locator)
            self.driver.find_element(*locator).click()

        except Exception as e:
            print("Exception", e)

    def enter_text(self, locator, textToEnter):

        try:
            time.sleep(2)
            self.wait_for_element(locator)
            time.sleep(1)
            self.driver.find_element(*locator).clear()
            self.driver.find_element(*locator).send_keys(textToEnter)

        except Exception as e:
            print("Exception", e)

    def select_dropdown_value(self, locator, selectText):

        try:
            self.wait_for_element(locator)
            select = Select(locator)
            # select by visible text
            select.select_by_visible_text(selectText)
            # select by value
            # select.select_by_value('1')

        except Exception as e:
            print("Exception", e)

    def select_dropdown_text(self, locator, selectText):

        try:
            self.wait_for_element(locator)
            dropdownlist = self.driver.find_elements(*locator)
            for element in dropdownlist:
                if element.text == selectText:
                    element.click()

        except Exception as e:
            print("Exception", e)

    def get_entry_intable(self, locator, text):
        try:
            self.wait_for_element(locator)
            table_id = self.driver.find_element(*locator)
            rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
            for row in rows[1:]:  # skip first row in table (Header row)
                # Get the columns (all the column 2)
                col = row.find_elements(By.TAG_NAME, "td")[2]
                if col.text == text:
                    return True
                return False

        except Exception as e:
            print("Exception ", e)

    def entry_present_intable(self, locator, text):
        try:
            #           self.wait_for_element(locator)
            self.enter_text(self.searchTextBox, text)
            time.sleep(2)
            table_id = self.driver.find_element(*locator)
            rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
            for row in rows[1:]:  # skip first row in table (Header row)
                # Get the columns (all the column 2)
                col = row.find_elements(By.TAG_NAME, "td")[0]
                if (col.text == "No data available."):
                    return False
                if locator == self.fleetTableId:
                    col = row.find_elements(By.TAG_NAME, "td")[1]
                    return True
                if locator == self.userTableId:
                    col = row.find_elements(By.TAG_NAME, "td")[2]
                    if col.text == text:
                        return True

        except Exception as e:
            print("Exception ", e)

    def get_text(self, locator):
        try:
            self.wait_for_element(locator)
            text = self.driver.find_element(*locator).text
            return text

        except Exception as e:
            print("Exception ", e)

    def element_is_visible(self, locator):
        try:
            # self.wait_for_element(locator)
            self.driver.find_element(*locator)

        except NoSuchElementException:
            return False
        return True
