from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap={
    "app" : "bs://f9a6ec9b8250ccdfc5c4d90bf69ec6620bf01a97",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    # Set other BrowserStack capabilities
    "bstack:options": {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "2nd Session",
        # Set your access credentials
        "userName": "shubhampatel_cyrG5Q",
        "accessKey": "3P77byxy2nJvECmSQuU4"
    }
}

driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

print(driver.page_source)

driver.quit()