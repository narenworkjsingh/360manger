import pytest
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from selenium.common.exceptions import NoSuchElementException as NE

# common base method used in framework
pytest.mark.usefixtures("getDriver")
class BaseTest:
    def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 15)

    # method for browser refresh
    def browserrefresh(self):
        self.driver.refresh()  

    # method for click operation on object
    def click(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator)).click()
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to click the element: {}".format(str(e)))    

    # method for entering values to input box
    def send_keys(self, by_locator, value):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            element.clear()
            element.send_keys(value)
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to send keys to the element: {}".format(str(e)))    

    # method to get value from text box
    def get_text(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("value")
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to get the element text: {}".format(str(e)))

    # method to wait for element
    def wait_for(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator))
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while waiting for the element: {}".format(str(e)))    

    # method tp assert assert text/message with expected result and print actual result.
    def assert_element(self, by_locator, text):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
    
        try:
            assert text in element.text
            print("Passed in Assertion" + "expecting for" + text + "but actual is" +element.text)
        except AssertionError:
            print("Failed in Assertion" + "expecting for" + text + "but actual is" +element.text)
            print(traceback.format_exc())    

    # method to fetch text from an object and return the text value
    def get_elmtext(self, by_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            return element.text 
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to get the element text: {}".format(str(e)))
    
    # method to check element visibilty and return true or false
    def check_element_visibilty(self, by_locator):
        try:
            assert self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except TE:
            return False
            


