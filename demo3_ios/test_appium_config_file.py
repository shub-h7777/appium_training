

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig():

    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
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


class Test_Ios(AppiumConfig):

    def test_click(self):
        self.driver.find_element(AppiumBy.NAME,"Text").click()
        self.driver.find_element(AppiumBy.NAME,"Text Input").send_keys("Shubham")
        self.driver.find_element(AppiumBy.XPATH,'(//XCUIElementTypeButton[@name="UI Elements"])[1]').click()
        self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Alert"]').click()
        alert_value=self.driver.find_element(AppiumBy.NAME,"This is a native alert.").text
        assert_that(alert_value).is_equal_to("This is a native alert.")
        self.driver.find_element(AppiumBy.NAME,"OK").click()

    # def test_click_alert(self):
    #     self.driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Alert"]').click()