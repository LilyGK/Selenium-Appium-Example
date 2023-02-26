import pytest
from selenium import webdriver
from os import environ
from selenium.webdriver.remote.remote_connection import RemoteConnection


@pytest.fixture(scope="class")
def selenium_driver(request):

    desired_caps = {}
    browser = {
        "platform": "Windows 10",
        "browserName": "Chrome",
        "browserversion": "108.0",
        "lang": "en"

    }
    desired_caps.update(browser)
    test_name = request.node.name
    build = environ.get('BUILD', "Wikipediatests")
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)
    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['build'] = build
    desired_caps['name'] = test_name
    desired_caps['video'] = True
    desired_caps['visual'] = True
    desired_caps['network'] = True
    desired_caps['console'] = True
    desired_caps['terminal'] = True
    caps = {"LT:Options": desired_caps}

    executor = RemoteConnection(selenium_endpoint)
    browser = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )
    request.cls.driver = browser
    yield browser
    browser.quit()
