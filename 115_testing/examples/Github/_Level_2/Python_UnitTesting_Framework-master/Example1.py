from selenium import webdriver
import unittest


class Internect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    def test_A_VerifyLink(self):
        URL = driver.current_url
        self.assertEqual(URL, 'http://the-internet.herokuapp.com/')

    def test_B_Title(self):
        Title=driver.title
        self.assertEqual(Title,'The Internet')

    @classmethod
    def tearDownClass(cls):
        driver.close()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
