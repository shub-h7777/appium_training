import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": r"C:\Users\150286\Python BootCamp\components\com.bsl.hyundai_2021-08-09.apk",
            "platformName": "Android",
            "deviceName": "Google Pixel 3",
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class Test_hyundai(AppiumConfig):
    def test_signup_page(self):
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/txt_signup").click()
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtFullname").send_keys("Shubham")
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtMobileNumber").send_keys("1234567891")
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtEmailAddress").send_keys("shubham@gmail")
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtPasswordRegis").send_keys("Password@123")
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtConfirmedPasswordRegis").send_keys("Password@123")
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/checkAcceptTermsCondition").click()
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/btnRegisterOnRegis").click()
        time.sleep(10)
