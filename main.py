import pytest
from selenium import webdriver

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_login_across_browsers(browser):
    capabilities = {
        "browserName": browser,
    }
    driver = webdriver.Remote("http://localhost:4444/wd/hub", capabilities)

    # Access page objects and perform login actions (using POM methods)
    # ...

    # Assertion for successful login across browsers
    # ...

    driver.quit()
