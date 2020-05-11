____ selenium ______ webdriver
______ u__
______ t___
____ selenium.webdriver.common.by ______ By


c_ Internet?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        Links _ driver.find_elements(By.TAG_NAME, "a")
        print("Total Number of Links", le.(Links))

        ___ morelinks __ Links:
            print(morelinks.text)

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ _____ __ _____
    ?.?
