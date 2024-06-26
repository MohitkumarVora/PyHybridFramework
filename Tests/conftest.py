from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# <------------------ pytest HTML Report --------------->
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "nop Commerce",
        "Module Name": "Customer",
        "Tester": "Mohit",
    }


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
