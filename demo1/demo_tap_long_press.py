import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": r"C:\Users\150286\Python BootCamp\components\khan-academy-7-3-2.apk",
            "platformName": "Android",
            "deviceName": "Google Pixel 3",
            "noReset": True
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()

class TestArts(AppiumConfig):
    def test_tap(self):
        if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        action=TouchAction(self.driver)
        action.tap(x=500,y=500,count=5).perform()

        time.sleep(5)

    def test_tap_using_webelement(self):
        if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()





