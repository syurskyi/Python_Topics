____ selenium ______ webdriver
______ u__
______ time

____ selenium.webdriver ______ ActionChains


c_ Auth?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

    ___ test_A_Drag_and_Drop
        source_page _ driver.find_element_by_id("box6")
        destination_location _ driver.find_element_by_id("box103")

        action _ ActionChains(driver)
        action.drag_and_drop(source_page, destination_location).perform()
        time.sleep(5)

    ___ test_B_clear
        re _ driver.find_element_by_id("box6")
        action _ ActionChains(driver)
        action.reset_actions()

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ __name__ __ '__main__':
    u__.main()
