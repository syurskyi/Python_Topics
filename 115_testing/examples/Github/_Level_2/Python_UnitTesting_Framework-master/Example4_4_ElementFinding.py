from selenium import webdriver
import unittest


class Links(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    def test_A_Links(self):
        driver.find_element_by_link_text("Add/Remove Elements").click()
        add = driver.find_element_by_xpath("//button[text()='Add Element']")

        for i in range(1, 5):
            add.click()

        Delete = driver.find_elements_by_xpath("//div[@id='elements']/button")
        for d in Delete:
            d.click()

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
