"""
Exercise 7: Testing your own app

This is a test file for the app created in Exercise 7. Since the app may
contain whatever content you like, the test provided initially is not very
specific: it only checks if the app contains a header element. You may use
the provided test as a model to add more specific tests for your app.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from exercise7.app import app
from test_utils import start_app, selenium_webdriver


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    """Set up the test module by starting the app."""
    start_app(app)
    return


def test_header_exists(selenium_webdriver):
    """Test if the app contains a header."""

    # Check if the header element exists
    try:
        header = selenium_webdriver.find_element(By.TAG_NAME, "h1")
    except NoSuchElementException:
        header = None
    assert header is not None, "Page should contain a Header element"
