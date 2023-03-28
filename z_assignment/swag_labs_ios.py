import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig():

    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://ce349708e017ea8d0a05c59c5f86402af60f66d7",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13.1",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "shubham_vMsZey",
                "accessKey": "PfytQFzr4F2xnm99CQfK",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()


class Test_Swag_Labs(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("John")
        self.driver.find_element(AppiumBy.NAME, "test-Password").send_keys("John123")
        self.driver.find_element(AppiumBy.NAME, "test-LOGIN").click()
        error_text = self.driver.find_element(AppiumBy.XPATH,
                                              '//XCUIElementTypeStaticText[@name="Username and password do not match any user in this service."]').text
        print(error_text)
        assert_that("Username and password do not match any user in this service.").is_equal_to(error_text)

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.NAME, "test-Password").send_keys("secret_sauce")
        self.driver.find_element(AppiumBy.NAME, "test-LOGIN").click()
        self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="test-ADD TO CART"])').click()
        self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="test-ADD TO CART"])').click()
        self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="test-ADD TO CART"])').click()
        self.driver.find_element(AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="test-ADD TO CART"])').click()


        # click on cart
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="test-Cart"]').click()

        #scroll to checkout
        para_dic={"direction": "down", "predicateString": "name=='test-CHECKOUT'", "toVisible": True}
        self.driver.execute_script("mobile: scroll", para_dic)


        self.driver.find_element(AppiumBy.NAME, "test-CHECKOUT").click()
        self.driver.find_element(AppiumBy.NAME, "test-First Name").send_keys("Shubham")
        self.driver.find_element(AppiumBy.NAME, "test-Last Name").send_keys("Patel")
        self.driver.find_element(AppiumBy.NAME, "test-Zip/Postal Code").send_keys("400001")
        self.driver.find_element(AppiumBy.NAME, "Return").click()

        self.driver.find_element(AppiumBy.NAME,"test-CONTINUE").click()



        card_details=self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"Payment Information")]').text
        print(card_details)


