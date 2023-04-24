import pytest
from selenium import webdriver
import datetime

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        #driver = webdriver.Chrome()
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launching chrome browser")
    else :
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        #driver = webdriver.Chrome()
        print("launching chrome browser")
    return driver

def pytest_configure(config):
    config._metadata ['Project Name'] = 'nop Commerce'
    config._metadata ['Module Name'] = 'Customer'
    config._metadata ['Tester'] = 'Tushar'

@pytest.mark.optionalhook
def pytest_metadata (metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
