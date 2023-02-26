import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os


@pytest.fixture(scope="class")
def appium_driver(request):

    options = UiAutomator2Options().load_capabilities({
        "app": "bs://03e7c2db1e8027a9381a14cce2c1a3ba55a18434",
        "platformVersion": "12.0",
        "deviceName": "Google Pixel 6",
        'bstack:options': {
            "projectName": "Mad Collective Test",
            "buildName": "Wikipedia test android",
            "sessionName": "Voyager 1 ",
            "userName": os.environ.get("BS_USERNAME"),
            "accessKey": os.environ.get("BS_ACCESS_KEY")
        }
    })

    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


