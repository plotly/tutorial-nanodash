"""
Exercise 4: Testing client-to-server communication (Frontend to Python)
"""
import time
from selenium.webdriver.common.by import By
import pytest
import json
import requests
from test_utils import (
    start_server, app_test_context, setup_fetch_interceptor,
    set_component_value, check_component_exists, wait_for_callback_completion
)


def test_state_endpoint_exists():
    """Test if the state endpoint exists and accepts POST requests."""
    start_server("exercise2/app.py")
    # Create a simple payload
    payload = {
        "trigger_id": "input-test",
        "state": {"input-test": "test value"}
    }
    
    # Send a POST request to the state endpoint
    response = requests.post(
        "http://127.0.0.1:5000/handle-change",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    # Check if the endpoint exists and accepts the request
    assert response.status_code != 404, "State endpoint should exist"
    assert response.status_code == 200, "State endpoint should accept POST requests"
    
    # Check if the response is valid JSON
    try:
        response_data = response.json()
        assert isinstance(response_data, dict), "Response should be a JSON object"
    except:
        pytest.fail("Response should be valid JSON")


def test_input_state_capture():
    """Test if component state changes are captured and sent to the server."""
    with app_test_context("exercise3/app.py") as driver:
        # Mock the fetch API to intercept the requests
        setup_fetch_interceptor(driver)
        
        # Check that components exist
        assert check_component_exists(driver, "input-test"), "Input component should exist"
        
        # Set input value using our utility
        test_text = "Hello, world!"
        assert set_component_value(driver, "input-test", test_text), "Should be able to set input value"
        
        payload = driver.execute_script("return window.lastPayload;")
        assert payload, "Request should be sent on input change"
        assert payload["trigger_id"] == "input-test", "trigger_id element ID should be correct"
        assert payload["state"]["input-test"] == test_text, "State should include the input value"


def test_multi_component_state():
    """Test if the state includes all component values."""
    with app_test_context("exercise4/app.py") as driver:
        # Mock the fetch API to intercept the requests
        setup_fetch_interceptor(driver)
        
        # Set input value using our utility
        assert set_component_value(driver, "input-test", "Text input value"), "Should be able to set input value"
        
        # Wait for callback to complete
        assert wait_for_callback_completion(driver), "Callback should complete"
        
        # Check payload
        payload = driver.execute_script("return window.lastPayload;")
        assert payload, "Request should be sent on input change"
        
        # Verify that all components are included in the state (even if not the triggered one)
        state = payload["state"]
        components_to_check = ["input-test"]  # Adjust based on your exercise
        for component_id in components_to_check:
            assert component_id in state, f"State should include {component_id}"
