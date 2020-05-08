from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By


class Internet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    def test_A_Links(self):
        Links = driver.find_elements(By.TAG_NAME, "a")
        print("Total Number of Links", len(Links))

        for morelinks in Links:
            print(morelinks.text)

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
