import pytest

# @pytest.mark.flaky(reruns=5)
# @pytest.mark.usefixtures("log_on_failure", "selenium_driver")


@pytest.mark.usefixtures("selenium_driver")
class BaseTest:

    def lambda_report(self, actual, expected):
        if actual == expected:
            self.driver.execute_script('lambda-status=passed')
        else:
            self.driver.execute_script('lambda-status=failed')
