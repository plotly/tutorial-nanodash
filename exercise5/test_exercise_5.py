"""
Exercise 5: Testing server-to-client communication (Python to Frontend)
"""

import pytest

from exercise5.app import app
from test_utils import (
    start_app,
    post_callback_request,
    verify_response_contents,
    selenium_webdriver,
)


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return


def test_first_callback_set():
    """Test the first set of components."""
    # Create a payload to simulate a component update for the first set
    name = "Danielle"
    color = "Purple"
    animal = "Turtle"
    payload = {
        "trigger_id": "name-textinput-1",
        "state": {
            "name-textinput-1": name,
            "color-dropdown-1": color,
            "animal-dropdown-1": animal,
        },
    }

    # Send a POST request to the state endpoint
    response = post_callback_request(payload)

    # Check if a callback was triggered and returned a response
    assert response, "Callback should return a response"

    # Check that the response is correct
    verify_response_contents(
        response,
        expected_response_contents={
            "textfield-output-1": f"{name} likes {color.lower()} {animal.lower()}s!",
        },
    )


def test_second_callback_set():
    """Test the second set of components."""
    # Create a payload to simulate a component update for the second set
    name = "Asha"
    color = "Orange"
    animal = "Dolphin"
    payload = {
        "trigger_id": "name-textinput-2",
        "state": {
            "name-textinput-2": name,
            "color-dropdown-2": color,
            "animal-dropdown-2": animal,
        },
    }

    # Send a POST request to the state endpoint
    response = post_callback_request(payload)

    # Check if a callback was triggered and returned a response
    assert response, "Callback should return a response"

    # Check that the response is correct
    verify_response_contents(
        response,
        expected_response_contents={
            "textfield-output-2": f"{name} likes {color.lower()} {animal.lower()}s!",
        },
    )
