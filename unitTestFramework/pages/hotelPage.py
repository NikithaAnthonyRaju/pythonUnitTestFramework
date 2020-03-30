import time

class HotelPage():
    def __init__(self, driver):
        self.driver = driver
        self.labelHotelName = "//span[contains(text(),'City / Hotel / Area / Building')]"
        self.inputHotelName = "//input[@placeholder='Enter city/ Hotel/ Area/ Building']"
        self.selectHotelName = "//p[contains(@class,'locusLabel appendBottom5')]"
        self.inputCheckin = "//input[@id='checkin']"
        self.inputCheckout = "//input[@id='checkout']"
        self.btnSearch = "//button[@id='hsw_search_button']"

    def validatePageTitle(self):
        assert self.driver.title == "MakeMyTrip.com: Save upto 60% on Hotel Booking 4,442,00+ Hotels Worldwide"

    def enterHotelDetails(self, hotelName, checkInDate, checkOutDate):
        driver = self.driver
        driver.find_element_by_xpath(self.labelHotelName).click()
        driver.find_element_by_xpath(self.inputHotelName).send_keys(hotelName)
        driver.find_element_by_xpath(self.selectHotelName).click()
        # driver.find_element_by_xpath(self.inputCheckin).click()
        # driver.find_element_by_xpath(self.inputCheckout).click(checkOutDate)
        # driver.find_element_by_xpath(self.btnSearch).click()