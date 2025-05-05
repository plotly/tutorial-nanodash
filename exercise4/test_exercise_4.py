"""
Exercise 4: Testing client-to-server communication (Frontend to Python)
"""

import pytest

from exercise4.app import app
from test_utils import (
    start_app,
    setup_fetch_interceptor,
    set_component_value,
    check_component_exists,
    get_component_value,
    verify_request_contents,
    selenium_webdriver,
)


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return


# Set up the interceptor which captures the
# requests sent by the client
@pytest.fixture(autouse=True)
def setup_selenium(selenium_webdriver):
    """Set up the fetch interceptor to capture requests."""
    setup_fetch_interceptor(selenium_webdriver)


def test_state_capture_dropdown_trigger(selenium_webdriver):
    """Test if component state changes are captured and sent to the server
    when the Dropdown component is changed."""

    # Make sure Dropdown component exists
    assert check_component_exists(selenium_webdriver, "card-suit"), (
        "Dropdown component should exist"
    )

    # Change Dropdown value
    new_value = "Diamonds"
    assert set_component_value(selenium_webdriver, "card-suit", new_value), (
        "Should be able to set dropdown value"
    )

    # Check that the new value is set correctly
    assert get_component_value(selenium_webdriver, "card-suit") == new_value, (
        "Dropdown value should be updated"
    )

    # Check that request is sent
    request_contents = selenium_webdriver.execute_script("return window.lastPayload;")
    assert request_contents, "Request should be sent on input change"

    # Check that request contains the correct info in the correct format
    verify_request_contents(
        request_contents,
        expected_trigger_id="card-suit",
        expected_state={
            "card-suit": new_value,
            "card-rank": get_component_value(selenium_webdriver, "card-rank"),
            "player-name": get_component_value(selenium_webdriver, "player-name"),
        },
    )


def test_state_capture_textinput_trigger(selenium_webdriver):
    """Test if component state changes are captured and sent to the server
    when the TextInput component is changed."""

    # Make sure TextInput component exists
    assert check_component_exists(selenium_webdriver, "player-name"), (
        "TextInput component should exist"
    )

    # Change TextInput value
    new_text = "Guido"
    assert set_component_value(selenium_webdriver, "player-name", new_text), (
        "Should be able to set input value"
    )

    # Check that the new value is set correctly
    assert get_component_value(selenium_webdriver, "player-name") == new_text, (
        "TextInput value should be updated"
    )

    # Check that request is sent
    request_contents = selenium_webdriver.execute_script("return window.lastPayload;")
    assert request_contents, "Request should be sent on input change"

    # Check that request contains the correct info in the correct format
    verify_request_contents(
        request_contents,
        expected_trigger_id="player-name",
        expected_state={
            "card-suit": get_component_value(selenium_webdriver, "card-suit"),
            "card-rank": get_component_value(selenium_webdriver, "card-rank"),
            "player-name": new_text,
        },
    )
