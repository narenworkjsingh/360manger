from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
from utility.utility import Utility
import time

class Customerpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in customer page 
    lst_customer = (By.XPATH, "//a[text()='Customers ']")
    lst_list = (By.XPATH, "//a[text()='List']")
    btn_addcustomer = (By.CSS_SELECTOR, "a.btn.btn-primary")
    edt_loginemail = (By.NAME, "email")
    edt_password = (By.NAME, "password")
    edt_name = (By.NAME, "name")
    edt_s3folder = (By.NAME, "s3_folder")
    btn_save = (By.ID, "save-customer")
    btn_cancel = (By.ID, "cancel")
    msg_errorvalidation = (By.XPATH, "//td[@colspan='2']")
    
# methods for customer page
# method to click on Customer menu option
    def click_customerlink(self):
        self.click(self.lst_customer)
        time.sleep(5)

# method to select list from customer menu dropdown
    def click_list(self):
        self.click(self.lst_list)
        time.sleep(2)


# method to click on add customer button
    def click_addcustomerbutton(self):
        self.click(self.btn_addcustomer)
        time.sleep(2)

# verify validation message showing up when save without required field 
    def check_validationmessage(self):
        validation_text = self.get_elmtext(self.msg_errorvalidation)
        print(validation_text)
        # Check if both required texts are present
        is_name_required_present = "Name is required." in validation_text
        is_s3_folder_required_present = "S3 folder is required." in validation_text
        # Validate both texts are present
        if is_name_required_present and is_s3_folder_required_present:
          assert True, "Both validation texts are present."
        else:
          assert False, "One or both validation texts are missing."   
    
# method to enter mandetory data to add customer page.
    def enterdata_customerpage(self, name, s3folder):
        self.send_keys(self.edt_name, name)
        self.send_keys(self.edt_s3folder, s3folder)
               
# method to update login value to testdata.json file
    def update_loginvalue(self):
            get_emailtext = self.get_text(self.edt_loginemail)
            print(get_emailtext)
            Utility.update_login_credentials(get_emailtext,"customerpage", "logincustomaer")
            get_passwordtext = self.get_text(self.edt_password)
            Utility.update_login_credentials(get_passwordtext,"customerpage", "loginpassword")
         

# method to click on save button  
    def click_savebutton(self):
        self.click(self.btn_save)
                 


