import pytest


@pytest.mark.usefixtures("appium_driver")
class BaseTest:
    pass
