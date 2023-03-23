import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": "bs://f9a6ec9b8250ccdfc5c4d90bf69ec6620bf01a97",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "shubhampatel_cyrG5Q",
                "accessKey": "3P77byxy2nJvECmSQuU4"
            }
        }
        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceCloud(AppiumConfig):

    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        print(self.driver.page_source)

    def test_invalid_sign_up_email_test(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        # click on setting icon
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Settings']").click()
        # click on sign in
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        # click on sign up with email
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'email')]").click()

        # send firstnamea as john -
        self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='First name']").send_keys("bala")
        # send lastname as peter -
        self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Last name']").send_keys("bala")

        # send birthday Aug 20, 1995 - Birthday
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").send_keys("August 20, 1995")
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").click()

        actual_text = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").text

        day_xpath = None
        month_xpath = None

        if len(actual_text) == 2:
            day_xpath = "//*[@resource-id='android:id/numberpicker_input']"
            month_xpath = "(//*[@resource-id='android:id/numberpicker_input'])[2]"
        else:
            month_xpath = "//*[@resource-id='android:id/numberpicker_input']"
            day_xpath = "(//*[@resource-id='android:id/numberpicker_input'])[2]"

        # choose Aug
        self.driver.find_element(AppiumBy.XPATH, month_xpath).click()
        self.driver.find_element(AppiumBy.XPATH, month_xpath).clear()
        self.driver.find_element(AppiumBy.XPATH, month_xpath).send_keys("Aug")

        # choose 20
        self.driver.find_element(AppiumBy.XPATH, day_xpath).click()
        self.driver.find_element(AppiumBy.XPATH, day_xpath).clear()
        self.driver.find_element(AppiumBy.XPATH, day_xpath).send_keys("20")

        # choose 1995
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys(
            "1995")

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()

        # send password as welcome123
        # send email as test123
        # click on create
        # assert the error message of mail id