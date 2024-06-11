from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Logout(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
 
#capture obhects in login page
    lnk_usernavbar = (By.ID, "navbar-login-menu")
    lnk_logout = (By.XPATH, "//a[text()='Log out']")


# method to click forgot password link
    def logout(self):
        self.click(self.lnk_usernavbar)
        self.click(self.lnk_logout)
