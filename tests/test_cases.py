import pytest
import time
from utility.utility import Utility
from pages.logout import Logout

@pytest.mark.usefixtures("getDriver")
class TestCases:

# test case to validate login functionality with invalid login and password
    def test_invalid_login_functionality(self, login_page):
        email = Utility.getjsondata('login', 'invalidemail')
        password = Utility.getjsondata('login', 'invalidpassword')
        login_page.login(email, password)
        login_page.verify_invalidlogin_message()

# test case to validate login functionality with valid email and password
    def test_valid_login_functionality(self, login_page):
        email = Utility.getjsondata('login', 'email')
        password = Utility.getjsondata('login', 'password')
        login_page.login(email, password)
        login_page.verify_homelink()

# test to verify that validation message display correctly when user hit save button without entering the required field
    def test_validation_messagedisplay(self, customer_page):
        customer_page.click_customerlink()
        customer_page.click_list()
        customer_page.click_addcustomerbutton()
        customer_page.click_savebutton()
        time.sleep(2)
        customer_page.check_validationmessage()

# test to verify new customer account gets created after entring the required data in cusotmer form
    def test_create_newcustomer(self, customer_page):
        name = Utility.generate_customerdata("customerpage", "name")
        s3folder = Utility.generate_customerdata("customerpage", "s3folder")
        customer_page.enterdata_customerpage(name, s3folder)
        customer_page.update_loginvalue()
        customer_page.click_savebutton()

# test to verify that user gets logged out successfully
    def test_logout_functionality(self):
        logoutpage = Logout(self.driver)
        logoutpage.logout()

# test to verify that user can login successfully with new account credential 
    def test_login_with_newaccount(self, login_page):
        newcustomer_email = Utility.getjsondata('customerpage', 'logincustomaer')
        newcustomer_password = Utility.getjsondata('customerpage', 'loginpassword')
        login_page.login(newcustomer_email, newcustomer_password)
        login_page.verify_homelink()
        logoutpage = Logout(self.driver)
        logoutpage.logout()
