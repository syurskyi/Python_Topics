from selenium import webdriver
import unittest
import requests



class Auth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    def test_A_Links(self):
        # driver.find_element_by_link_text("Broken Images").click()
        # time.sleep(4)
        # alert = driver.switch_to_alert()
        # alert.dismiss()

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
