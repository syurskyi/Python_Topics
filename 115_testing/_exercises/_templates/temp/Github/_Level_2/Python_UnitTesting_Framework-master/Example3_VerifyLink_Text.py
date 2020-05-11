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
        driver.find_element_by_link_text("A/B Testing").click()
        driver.implicitly_wait(5)
        ABTestURL _ driver.current_url

        aE..(ABTestURL, 'http://the-internet.herokuapp.com/abtest')

        TextComparsion _ driver.find_element_by_xpath("//p")
        aE..(TextComparsion.text,
                         'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through).')

        print(TextComparsion.text)

    @classmethods
    ___ tearDownClass ___
        driver.quit()
        print("Close Application")


__ _____ __ _____
    ?.?
