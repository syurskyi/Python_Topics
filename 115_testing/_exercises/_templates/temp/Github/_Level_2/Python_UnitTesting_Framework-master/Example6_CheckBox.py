from selenium import webdriver
import unittest
import time


c_ Auth(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com")

    # def test_A_RadiButton(self):
    #     driver.get("https://www.facebook.com/")
    #     print(driver.find_element_by_id("u_0_9").is_selected())
    #     driver.find_element_by_id("u_0_9").click()
    #     print(driver.find_element_by_id("u_0_9").is_selected())

    ___ test_B_CheckBox(self):
        driver.find_element_by_link_text("Checkboxes").click()
        print(driver.find_element_by_xpath("//div[@class='example']/form/input[1]").is_selected())
        driver.find_element_by_xpath("//div[@class='example']/form/input[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='example']/form/input[2]").click()
        time.sleep(3)

    @classmethod
    ___ tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
