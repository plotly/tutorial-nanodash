"""
Exercise 1: Testing the basic Flask server with static HTML capabilities
"""
import requests
import pytest

from exercise1.app import app
from test_utils import start_app


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return

def test_page_structure():
    """Test if the Flask server is running and returning HTML content."""

    # Check if the server is running and responding to requests
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200

    # Check if the response contains HTML content
    assert "<html>" in response.text, "Response does not contain HTML"

    # Check if the page contains a title
    assert "<title>" in response.text, "Response does not contain a title"
