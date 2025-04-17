"""
Exercise 5: Testing server-to-client communication (Python to Frontend)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import pytest
import requests
import time
from test_utils import start_server


def test_callback_registration():
    """Test if callbacks can be registered and processed."""
    start_server("exercise5/app.py")
    # Create a payload to simulate a component update
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
    
    # Check if a callback was triggered and returned a response
    assert response.status_code == 200
    response_data = response.json()
    assert response_data, "Callback should return a response"
    
    # Assuming a simple echo callback that returns the input value in an output component
    assert "output-test" in response_data, "Output component should be in the response"
    assert response_data["output-test"] == "test value", "Callback should process input value"


def test_callback_function_execution():
    """Test if the callback function is executed with the correct inputs."""
    process = start_server("exercise5/app.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Set up response tracking
        driver.execute_script("""
            window.lastResponse = null;
            const originalFetch = window.fetch;
            window.fetch = function(url, options) {
                return originalFetch(url, options).then(response => {
                    if (url === '/handle-change') {
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


def test_multiple_callbacks():
    """Test if multiple callbacks can be registered and executed correctly."""
    start_server("exercise5/app.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Set up response tracking
        driver.execute_script("""
            window.allResponses = [];
            const originalFetch = window.fetch;
            window.fetch = function(url, options) {
                return originalFetch(url, options).then(response => {
                    if (url === '/handle-change') {
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
        dropdown_element = Select(driver.find_element(By.ID, "dropdown-test"))
        dropdown_element.select_by_visible_text('Option 2')
        time.sleep(1)
        
        # Get all responses
        responses = driver.execute_script("return window.allResponses;")
        assert len(responses) >= 2, "Should receive responses for both inputs"
        
        # Check if the callbacks were independent
        # This assumes the second response includes the dropdown output
        print('here', responses)
        assert "dropdown-output" in responses[len(responses) - 1], "Second callback should update dropdown output"
    finally:
        driver.quit()


if __name__ == "__main__":
    test_callback_registration()
    test_callback_function_execution()
    test_multiple_callbacks()