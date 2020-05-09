____ selenium ______ webdriver
______ u__
______ time
____ selenium.webdriver.common.by ______ By


c_ Internet?.?

    @classmethod
    ___ setUpClass(cls
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        Links _ driver.find_elements(By.TAG_NAME, "a")
        print("Total Number of Links", len(Links))

        for morelinks in Links:
            print(morelinks.text)

    @classmethod
    ___ tearDownClass(cls
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    u__.main()
