____ selenium ______ webdriver
______ u__
______ t___
____ selenium.webdriver ______ ActionChains
____ selenium.webdriver.common.keys ______ Keys


c_ MouseOver?.?

    ??
    ___ setUpClass ___
        global driver
        driver _ webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com")

    ___ test_A_Login
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").send_keys(Keys.ENTER)

    # This is the example for the hover the mouse

    ___ test_B_Mouse
        Admin _ driver.find_element_by_id("menu_admin_viewAdminModule")
        UserManagement _ driver.find_element_by_id("menu_admin_UserManagement")
        Users _ driver.find_element_by_id("menu_admin_viewSystemUsers")

        action _ ActionChains(driver)
        action.move_to_element(Admin).move_to_element(UserManagement).move_to_element(Users).click().perform()
        t___.sleep(5)

    # This is the example for the double click

    ___ test_C_DoubleClick
        Dashboard _ driver.find_element_by_id("menu_dashboard_index")
        action _ ActionChains(driver)
        action.move_to_element(Dashboard).double_click().perform()
        t___.sleep(4)

    # This is the example for the context_click

    ___ test_D_Context
        AssingLeave _ driver.find_element_by_class_name("quickLaunge")
        action _ ActionChains(driver)
        action.move_to_element(AssingLeave).context_click().send_keys(Keys.ARROW_DOWN).click().perform()

    ??
    ___ tearDownClass ___
        # driver.quit()
        print("Close Application")


__ _____ __ _____
    ?.?
