____ selenium ______ webdriver
______ unittest


c_ Auth(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://demo.automationtesting.in/FileDownload.html")
        driver.fullscreen_window()

    ___ test_A_UploadFile
        driver.switch_to_frame(0)
        Upload _ driver.find_element_by_id("RESULT_FileUpload-11")
        Upload.send_keys("/Users/reenupanwar/Desktop/Sri.jpg")

    @classmethod
    ___ tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
