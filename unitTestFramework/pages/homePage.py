class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.tabFlights = "//span[text()='Flights']"
        self.tabHotels = "//span[text()='Hotels']"

    def validatePageTitle(self):
        assert self.driver.title == "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"

    def clickOnHotels(self):
        self.driver.find_element_by_xpath(self.tabHotels).click()

    def clickOnFlights(self):
        self.driver.find_element_by_xpath(self.tabFlights).click()