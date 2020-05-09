____ selenium ______ webdriver
______ unittest


c_ Internect(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_VerifyLink
        URL _ driver.current_url
        assertEqual(URL, 'http://the-internet.herokuapp.com/')

    ___ test_B_Title
        Title_driver.title
        assertEqual(Title,'The Internet')

    @classmethod
    ___ tearDownClass(cls):
        driver.close()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
