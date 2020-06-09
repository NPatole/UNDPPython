import time
from pageObjects.Fleets import Fleets
from tests.conftest import BaseClass, driver



class TestFleets(BaseClass):
    fleets = Fleets(driver)

    def test_navigateToFleetMenu(self):
        if not TestFleets.fleets.element_is_visible(TestFleets.fleets.configActiveMenu):
            TestFleets.fleets.click_on_button(TestFleets.fleets.tenantDropDown)
            TestFleets.fleets.select_dropdown_text(TestFleets.fleets.teanantList, self.configfileParser("Tenant"))
            TestFleets.fleets.click_on_button(TestFleets.fleets.configMenu)
        assert ("test" == "testing")


    def test_addFleet(self):
        TestFleets.fleets.click_on_button(TestFleets.fleets.fleetsMenu)
        if TestFleets.fleets.entry_present_intable(TestFleets.fleets.fleetTableId, self.configfileParser("FleetName")) == True :
            TestFleets.fleets.deleteFleet()
        TestFleets.fleets.addFleet()
        assert TestFleets.fleets.entry_present_intable(TestFleets.fleets.fleetTableId, self.configfileParser("FleetName")) == True

    def test_deleteFleet(self):
        TestFleets.fleets.click_on_button(TestFleets.fleets.fleetsMenu)
        if TestFleets.fleets.entry_present_intable(TestFleets.fleets.fleetTableId, self.configfileParser("FleetName")) == False :
            TestFleets.fleets.addFleet()
        TestFleets.fleets.deleteFleet()
        assert (TestFleets.fleets.get_text(TestFleets.fleets.alertDialog) == "Baner has been deleted successfully.")


