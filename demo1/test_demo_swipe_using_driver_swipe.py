import base64
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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
        self.driver.start_recording_screen()
        yield
        encoded = self.driver.stop_recording_screen()
        open("recording.mp4", "wb").write(base64.b64decode(encoded))
        self.driver.quit()

class TestArts(AppiumConfig):
    def test_the_himalayas_topics(self):
        # if len(self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")')) == 1:
        #     self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()
        self.driver.implicitly_wait(1)
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Art of Asia']")) == 0:
            self.driver.swipe(902, 1174, 902, 794, 600)

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Art of Asia']").click()
        self.driver.implicitly_wait(30)

        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[contains(@text,'Himal')]")) == 0:
            self.driver.swipe(902, 1174, 902, 794, 600)

        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Himal')]").click()
        self.driver.implicitly_wait(30)

        time.sleep(5)
