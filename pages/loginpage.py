from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time


class Loginpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture obhects in login page
    
    edt_email = (By.NAME, "email")
    edt_password = (By.NAME, "password")
    btn_login = (By.NAME, "submit")
    lnk_usernavbar = (By.ID, "navbar-login-menu")
    lnk_logout = (By.CSS_SELECTOR, 'a[href="/logout?_acid=3965"]')
    lnk_home = (By.ID, "navbar-home-link")
    msg_invalid_login = (By.XPATH, "//li[text()='Invalid username or password']")

# methods for login page

# method for login 
    def login(self, email, password):
        self.send_keys(self.edt_email, email)
        self.send_keys(self.edt_password, password)
        self.click(self.btn_login)
        time.sleep(5)

# method for verifying home page display after login
    def verify_homelink(self):
        result = self.check_element_visibilty(self.lnk_home)
        if (result == True):
            assert True, "login attempt with new use is successful"
        else:
            assert False, "Failed to login"
            
# method to verify message display for invalid login
    def verify_invalidlogin_message(self):
        self.assert_element(self.msg_invalid_login, 'Invalid username or password')