import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": r"C:\Users\150286\Python BootCamp\components\khan-academy-7-3-2.apk",
            "platformName": "Android",
            "deviceName": "Google Pixel 3",
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceCloud(AppiumConfig):
    def test_login(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'UiSelector().text("Enter an e-mail address or username")').send_keys("Shubham")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Password")').send_keys("Password")
        self.driver.find_element(AppiumBy.XPATH, '(//*[@text="Sign in"])[2]').click()
        error_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                              'UiSelector().text("There was an issue signing in")').text
        assert_that(error_text).is_equal_to("There was an issue signing in")
