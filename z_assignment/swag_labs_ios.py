import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig():

    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://043b78b811594e7ccc9cce0ff27c94788ba47c6e",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13.1",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "shubham_IABeCR",
                "accessKey": "Mppd3EzBym4j9FPUq8ui",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(5)
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
