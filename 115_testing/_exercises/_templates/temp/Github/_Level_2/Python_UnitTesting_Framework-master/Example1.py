____ selenium ______ webdriver
______ u__


c_ Internect?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_VerifyLink
        URL _ driver.current_url
        aE..(URL, 'http://the-internet.herokuapp.com/')

    ___ test_B_Title
        Title_driver.title
        aE..(Title,'The Internet')

    ??
    ___ tearDownClass ___
        driver.close()
        print("Close Application")


__ _____ __ _____
    ?.?
