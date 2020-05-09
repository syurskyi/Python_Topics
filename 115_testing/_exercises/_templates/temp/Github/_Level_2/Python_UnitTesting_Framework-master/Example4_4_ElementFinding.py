____ selenium ______ webdriver
______ u__


c_ Links?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        driver.find_element_by_link_text("Add/Remove Elements").click()
        add _ driver.find_element_by_xpath("//button[text()='Add Element']")

        for i __ range(1, 5
            add.click()

        Delete _ driver.find_elements_by_xpath("//div[@id='elements']/button")
        for d __ Delete:
            d.click()

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ __name__ __ '__main__':
    ?.?
