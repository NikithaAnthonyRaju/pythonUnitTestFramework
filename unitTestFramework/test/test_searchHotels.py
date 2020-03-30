from selenium import webdriver
import time
import unittest
import os
import HtmlTestRunner

from unitTestFramework.pages.homePage import HomePage
from unitTestFramework.pages.hotelPage import HotelPage

class SearchHotelsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'drivers\\chromedriver.exe'))
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_search_hotels(self):
        driver = self.driver
        driver.get("https://www.makemytrip.com/")
        time.sleep(10)

        home = HomePage(driver)
        home.validatePageTitle()
        home.clickOnHotels()
        time.sleep(10)

        hotel = HotelPage(driver)
        hotel.validatePageTitle()
        hotel.enterHotelDetails("JW Marriot Bengaluru", "03 Mar", "05 Mar")

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Execution Completed")

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/anthonpa/PycharmProjects/practice/unitTestFramework/reports"))
