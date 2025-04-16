"""
Exercise 5: Testing server-to-client communication (Python to Frontend)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import json
import requests
import time
from .test_utils import start_server, stop_server


def test_callback_registration():
    """Test if callbacks can be registered and processed."""
    process = start_server("tests/exercise_apps/exercise5.py")
    try:
        # Create a payload to simulate a component update
        payload = {
            "triggered": "input-test",
            "state": {"input-test": "test value"}
        }
        
        # Send a POST request to the state endpoint
        response = requests.post(
            "http://127.0.0.1:5000/state",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        # Check if a callback was triggered and returned a response
        assert response.status_code == 200
        response_data = response.json()
        assert response_data, "Callback should return a response"
        
        # Assuming a simple echo callback that returns the input value in an output component
        assert "output-test" in response_data, "Output component should be in the response"
        assert response_data["output-test"] == "test value", "Callback should process input value"
    finally:
        stop_server(process)


def test_callback_function_execution():
    """Test if the callback function is executed with the correct inputs."""
    process = start_server("tests/exercise_apps/exercise5.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Set up response tracking
        driver.execute_script("""
            window.lastResponse = null;
            const originalFetch = window.fetch;
            window.fetch = function(url, options) {
                return originalFetch(url, options).then(response => {
                    if (url === '/state') {
                        return response.clone().json().then(data => {
                            window.lastResponse = data;
                            return response;
                        });
                    }
                    return response;
                });
            };
        """)
        
        # Find and modify the input
        input_element = driver.find_element(By.ID, "input-test")
        test_value = "Testing callback"
        input_element.clear()
        input_element.send_keys(test_value)
        
        # Wait for the response to be processed
        time.sleep(2)
        
        # Check if the response was captured and contains the right information
        response = driver.execute_script("return window.lastResponse;")
        assert response, "Response should be received from the server"
        
        # Check if the callback processed the input correctly
        # This assumes a callback that echoes the input to the output-test
        assert "output-test" in response, "Response should include the output component ID"
        assert response["output-test"] == test_value, "Callback should process the input correctly"
    finally:
        driver.quit()
        stop_server(process)


def test_multiple_callbacks():
    """Test if multiple callbacks can be registered and executed correctly."""
    process = start_server("tests/exercise_apps/exercise5.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Set up response tracking
        driver.execute_script("""
            window.allResponses = [];
            const originalFetch = window.fetch;
            window.fetch = function(url, options) {
                return originalFetch(url, options).then(response => {
                    if (url === '/state') {
                        return response.clone().json().then(data => {
                            window.allResponses.push(data);
                            return response;
                        });
                    }
                    return response;
                });
            };
        """)
        
        # Test the first callback
        input_element = driver.find_element(By.ID, "input-test")
        input_element.clear()
        input_element.send_keys("Input 1")
        time.sleep(1)
        
        # Test the second callback
        dropdown_element = driver.find_element(By.ID, "dropdown-test")
        dropdown_options = dropdown_element.find_elements(By.TAG_NAME, "option")
        dropdown_options[1].click()  # Select the second option
        time.sleep(1)
        
        # Get all responses
        responses = driver.execute_script("return window.allResponses;")
        assert len(responses) >= 2, "Should receive responses for both inputs"
        
        # Check if the callbacks were independent
        # This assumes the second response includes the dropdown output
        assert "dropdown-output" in responses[1], "Second callback should update dropdown output"
    finally:
        driver.quit()
        stop_server(process)


if __name__ == "__main__":
    test_callback_registration()
    test_callback_function_execution()
    test_multiple_callbacks()