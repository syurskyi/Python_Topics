from selenium import webdriver
import unittest
import time

from selenium.webdriver import ActionChains


class Auth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

    def test_A_Drag_and_Drop(self):
        source_page = driver.find_element_by_id("box6")
        destination_location = driver.find_element_by_id("box103")

        action = ActionChains(driver)
        action.drag_and_drop(source_page, destination_location).perform()
        time.sleep(5)

    def test_B_clear(self):
        re = driver.find_element_by_id("box6")
        action = ActionChains(driver)
        action.reset_actions()

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
