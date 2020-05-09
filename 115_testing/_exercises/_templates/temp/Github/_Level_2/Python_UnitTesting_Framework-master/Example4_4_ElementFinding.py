____ selenium ______ webdriver
______ unittest


c_ Links(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        driver.find_element_by_link_text("Add/Remove Elements").click()
        add _ driver.find_element_by_xpath("//button[text()='Add Element']")

        for i in range(1, 5):
            add.click()

        Delete _ driver.find_elements_by_xpath("//div[@id='elements']/button")
        for d in Delete:
            d.click()

    @classmethod
    ___ tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
