from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MouseOver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com")

    def test_A_Login(self):
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").send_keys(Keys.ENTER)

    # This is the example for the hover the mouse

    def test_B_Mouse(self):
        Admin = driver.find_element_by_id("menu_admin_viewAdminModule")
        UserManagement = driver.find_element_by_id("menu_admin_UserManagement")
        Users = driver.find_element_by_id("menu_admin_viewSystemUsers")

        action = ActionChains(driver)
        action.move_to_element(Admin).move_to_element(UserManagement).move_to_element(Users).click().perform()
        time.sleep(5)

    # This is the example for the double click

    def test_C_DoubleClick(self):
        Dashboard = driver.find_element_by_id("menu_dashboard_index")
        action = ActionChains(driver)
        action.move_to_element(Dashboard).double_click().perform()
        time.sleep(4)

    # This is the example for the context_click

    def test_D_Context(self):
        AssingLeave = driver.find_element_by_class_name("quickLaunge")
        action = ActionChains(driver)
        action.move_to_element(AssingLeave).context_click().send_keys(Keys.ARROW_DOWN).click().perform()

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
