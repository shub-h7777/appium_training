import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "android",
    "deviceName": "realme 8",
    "app": r"C:\Users\150286\Python BootCamp\components\khan-academy-7-3-2.apk"
}

driver=webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)



print(driver.page_source)

time.sleep(5)
driver.quit()