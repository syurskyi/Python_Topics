from selenium import webdriver
import unittest


class Auth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://testautomationpractice.blogspot.com/")
        driver.fullscreen_window()

    def test_A_UploadFile(self):
        driver.switch_to_frame(0)
        Upload = driver.find_element_by_id("RESULT_FileUpload-11")
        Upload.send_keys("/Users/reenupanwar/Desktop/Sri.jpg")

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
