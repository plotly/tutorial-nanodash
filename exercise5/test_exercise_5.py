"""
Exercise 5: Testing server-to-client communication (Python to Frontend)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import pytest
import requests
import time

from exercise5.app import app
from test_utils import start_app, selenium_webdriver, set_component_value

# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return

def test_callback_registration():
    """Test if callbacks can be registered and processed."""
    # Create a payload to simulate a component update
    new_text = "Hello World!"
    payload = {
        "trigger_id": "chart-title-input",
        "state": {
            "chart-title-input": new_text,
            "year-dropdown": "2022",
            "month-dropdown": "January",
            "center-name-dropdown": "All",
        },
    }
    
    # Send a POST request to the state endpoint
    response = requests.post(
        "http://127.0.0.1:5000/handle-change",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    # Check if a callback was triggered and returned a response
    assert response.status_code == 200
    response_data = response.json()
    assert response_data, "Callback should return a response"
    
    # Assuming a simple echo callback that returns the input value in an output component
    assert "attendance-graph" in response_data, "Output component should be in the response"
    assert new_text in str(response_data["attendance-graph"]), "Figure returned by callback should contain input text"
