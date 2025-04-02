"""
pytest configuration file for nanodash tests
"""
import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    """Add command-line options for pytest."""
    parser.addoption(
        "--app-path", action="store", default=None, help="Path to the application script"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )


@pytest.fixture(scope="function")
def selenium_driver(request):
    """Setup and teardown for Selenium WebDriver."""
    headless = request.config.getoption("--headless")
    
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    
    # Create the driver
    driver = webdriver.Chrome(options=options)
    
    # Add wait time
    driver.implicitly_wait(5)
    
    # Return the driver for the test
    yield driver
    
    # Teardown
    driver.quit()


@pytest.fixture(scope="function")
def wait_for(selenium_driver):
    """Helper function to wait for a condition."""
    def _wait_for(condition_function, timeout=10):
        start_time = time.time()
        while time.time() < start_time + timeout:
            if condition_function():
                return True
            time.sleep(0.1)
        return False
    
    return _wait_for