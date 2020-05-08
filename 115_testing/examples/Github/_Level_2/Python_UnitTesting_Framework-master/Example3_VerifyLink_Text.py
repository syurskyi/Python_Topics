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
        driver.find_element_by_link_text("A/B Testing").click()
        driver.implicitly_wait(5)
        ABTestURL = driver.current_url

        self.assertEqual(ABTestURL, 'http://the-internet.herokuapp.com/abtest')

        TextComparsion = driver.find_element_by_xpath("//p")
        self.assertEqual(TextComparsion.text,
                         'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through).')

        print(TextComparsion.text)

    @classmethods
    def tearDownClass(cls):
        driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
