____ selenium ______ webdriver
______ u__


c_ Auth?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://demo.automationtesting.in/FileDownload.html")
        driver.fullscreen_window()

    ___ test_A_UploadFile
        driver.switch_to_frame(0)
        Upload _ driver.find_element_by_id("RESULT_FileUpload-11")
        Upload.send_keys("/Users/reenupanwar/Desktop/Sri.jpg")

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ _____ __ _____
    ?.?
