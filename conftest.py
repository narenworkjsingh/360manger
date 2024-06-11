import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from pages.loginpage import Loginpage
from pages.coustomerpage import Customerpage

# Add command line option for browser choice
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser to use for tests. Default is 'chrome'.")

@pytest.fixture(scope="class")
def getBrowser(request):
    browser = request.config.getoption("--browser")
    return browser

#code to get the browser from command line and run the code by default option is chrome
@pytest.fixture(scope="class")
def getDriver(request, getBrowser):
    if getBrowser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif getBrowser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("https://testautomationchallenge-manager.testenv.impel.io")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    time.sleep(10)
    driver.quit()

# Fixture for login page
@pytest.fixture
def login_page(getDriver):
    return Loginpage(getDriver)

# Fixture for customer page
@pytest.fixture
def customer_page(getDriver):
    return Customerpage(getDriver)

# Code to publish the result as html report
def pytest_html_report_title(report):
    report.title = "360manager test execution report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url("https://testautomationchallenge-manager.testenv.impel.io"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('getDriver')
            screenshot_path = f'C:/DemoTest/reports/failure_{timestamp}.png'
            driver.save_screenshot(screenshot_path)
            extra.append(pytest_html.extras.image(screenshot_path))
        elif report.passed:
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('getDriver')
            screenshot_path = f'C:/DemoTest/reports/success_{timestamp}.png'
            driver.save_screenshot(screenshot_path)
            extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra
