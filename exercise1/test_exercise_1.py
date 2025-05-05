"""
Exercise 1: Testing the basic Flask server with static HTML capabilities
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

from exercise1.app import app
from test_utils import start_app


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return

def test_page_structure(selenium_webdriver):
    """Test if the Flask server is running and returning HTML content."""

    # Check if the page returns valid HTML
    try:
        page_full_html = selenium_webdriver.find_element(By.TAG_NAME, "html")
    except NoSuchElementException:
        page_full_html = None
    assert page_full_html is not None, "Page should contain HTML element"

    # Check if the page contains a title
    assert selenium_webdriver.title, "Page should have a title"
