from selenium import webdriver
import unittest


c_ Auth(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://demo.automationtesting.in/FileDownload.html")
        driver.fullscreen_window()

    ___ test_A_UploadFile(self):
        driver.switch_to_frame(0)
        Upload = driver.find_element_by_id("RESULT_FileUpload-11")
        Upload.send_keys("/Users/reenupanwar/Desktop/Sri.jpg")

    @classmethod
    ___ tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
