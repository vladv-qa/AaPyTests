from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time
import data

class AirArabiaSharajahLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(data.path)
        self.driver.set_window_position(0,50)
        self.driver.set_window_size(1700, 600)
        self.driver.get('https://www.airarabia.com/en')

        time.sleep(5)

    def test_sharajah_login(self):
        driver = self.driver
        login_link = driver.find_element_by_class_name('show-for-large.red-text')
        login_link.click()

        time.sleep(5)

        sharjah_accordion = driver.find_element_by_class_name('ui-accordion-header.ui-helper-reset.ui-state-default.ui-accordion-icons.ui-corner-all')
        sharjah_accordion.click()
        time.sleep(1)
        sharajah_link = driver.find_element_by_link_text("Click here")
        sharajah_link.click()

        time.sleep(2)
        try:
            login_field = driver.find_element_by_name('email')
            login_field.send_keys(data.email_sharjah)
            password_field = driver.find_element_by_name('password')
            password_field.send_keys(data.pass_sharjah)
            time.sleep(2)
            login_button = driver.find_element_by_name('loginButton')
            login_button.click()
            time.sleep(10)
            if "Mr. Test Selenium" in driver.find_element_by_class_name('login-name.ng-binding').text:
                print("User has been LOGGED!")
                time.sleep(10)

        finally:
            driver.quit()

# pass_field = driver.find_element_by_class_name('form-control.ng-isolate-scope.ng-valid-pattern.ng-valid-minlength.ng-dirty.ng-valid-parse ng-valid.ng-valid-required.ng-touched')
# pass_field.send_keys(data.pass_sharjah)

# time.sleep(2)

def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
    unittest.main()