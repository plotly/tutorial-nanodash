"""
Exercise 4: Testing client-to-server communication (Frontend to Python)
"""
import pytest
import requests

from exercise4.app import app
from test_utils import (
    start_app, setup_fetch_interceptor,
    set_component_value, check_component_exists, wait_for_callback_completion, selenium_webdriver,
)

# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return


def test_input_state_capture(selenium_webdriver):
    """Test if component state changes are captured and sent to the server."""
    # Mock the fetch API to intercept the requests
    setup_fetch_interceptor(selenium_webdriver)
    
    # Make sure TextInput component exists
    assert check_component_exists(selenium_webdriver, "chart-title-input"), "TextInput component should exist"
    
    # Change TextInput value
    new_text = "Hello, world!"
    assert set_component_value(selenium_webdriver, "chart-title-input", new_text), "Should be able to set input value"
    
    # Check that request is sent
    request_contents = selenium_webdriver.execute_script("return window.lastPayload;")
    assert request_contents, "Request should be sent on input change"
    
    # Check that request contains the correct info in the correct format
    assert "trigger_id" in request_contents, "Request should contain `trigger_id` key"
    assert "state" in request_contents, "Request should contain `state` key"
    state = request_contents["state"]
    assert request_contents["trigger_id"] == "chart-title-input", "trigger_id element ID should be correct"
    input_component_ids = [
        "year-dropdown",
        "month-dropdown",
        "center-name-dropdown",
        "chart-title-input",
    ]
    state = request_contents["state"]
    for component_id in input_component_ids:
            assert component_id in state, f"State should include component with ID `{component_id}`"
