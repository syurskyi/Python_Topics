____ selenium ______ webdriver
______ u__
______ requests



c_ Auth?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        # driver.find_element_by_link_text("Broken Images").click()
        # time.sleep(4)
        # alert = driver.switch_to_alert()
        # alert.dismiss()

        links _ driver.find_elements_by_css_selector("a")
        ___ link __ links:
            r _ requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ _____ __ _____
    ?.?
