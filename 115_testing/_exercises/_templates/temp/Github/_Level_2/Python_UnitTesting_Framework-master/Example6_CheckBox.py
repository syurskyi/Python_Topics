____ selenium ______ webdriver
______ u__
______ t___


c_ Auth?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com")

    # def test_A_RadiButton(self):
    #     driver.get("https://www.facebook.com/")
    #     print(driver.find_element_by_id("u_0_9").is_selected())
    #     driver.find_element_by_id("u_0_9").click()
    #     print(driver.find_element_by_id("u_0_9").is_selected())

    ___ test_B_CheckBox
        driver.find_element_by_link_text("Checkboxes").click()
        print(driver.find_element_by_xpath("//div[@class='example']/form/input[1]").is_selected())
        driver.find_element_by_xpath("//div[@class='example']/form/input[1]").click()
        t___.sleep(3)
        driver.find_element_by_xpath("//div[@class='example']/form/input[2]").click()
        t___.sleep(3)

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ _____ __ _____
    ?.?
