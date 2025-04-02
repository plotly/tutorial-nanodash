"""
Exercise 4c: Testing UI updates from callback responses
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from .test_utils import start_server, stop_server


def test_text_updates():
    """Test if text outputs are updated correctly."""
    process = start_server("tests/exercise_apps/exercise4c.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Find input and output elements
        input_element = driver.find_element(By.ID, "input-test")
        
        # Send value to the input
        test_value = "Updated text"
        input_element.clear()
        input_element.send_keys(test_value)
        
        # Wait for the callback to process and update the UI
        time.sleep(1)
        
        # Check if the output element was updated
        output_element = driver.find_element(By.ID, "output-test")
        assert output_element.get_attribute("value") == test_value, "Output should be updated with input value"
    finally:
        driver.quit()
        stop_server(process)


def test_graph_updates():
    """Test if graph components are updated correctly."""
    process = start_server("tests/exercise_apps/exercise4c.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Wait for Plotly graph to be initialized
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#graph-test .main-svg")))
        
        # Get initial title
        initial_title = None
        try:
            title_element = driver.find_element(By.CSS_SELECTOR, "#graph-test .gtitle")
            initial_title = title_element.text
        except:
            pass  # Title might not exist initially
        
        # Update the input that should trigger a graph update
        input_element = driver.find_element(By.ID, "graph-input")
        test_value = "New Graph Title"
        input_element.clear()
        input_element.send_keys(test_value)
        
        # Wait for the graph to update
        time.sleep(2)
        
        # Check if the graph title was updated
        try:
            title_element = driver.find_element(By.CSS_SELECTOR, "#graph-test .gtitle")
            new_title = title_element.text
            assert new_title == test_value, "Graph title should be updated to match input"
            if initial_title:
                assert new_title != initial_title, "Graph title should have changed"
        except:
            pytest.fail("Graph title should be updated and visible")
    finally:
        driver.quit()
        stop_server(process)


def test_multiple_output_updates():
    """Test if multiple outputs can be updated from a single input."""
    process = start_server("tests/exercise_apps/exercise4c.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Find the trigger input
        multi_input = driver.find_element(By.ID, "multi-output-input")
        test_value = "Multi Update"
        multi_input.clear()
        multi_input.send_keys(test_value)
        
        # Wait for updates to propagate
        time.sleep(1)
        
        # Check if all outputs were updated
        output1 = driver.find_element(By.ID, "output-1")
        output2 = driver.find_element(By.ID, "output-2")
        
        # Different verification based on component types, this assumes text fields
        assert test_value in output1.get_attribute("value"), "First output should be updated"
        assert test_value in output2.get_attribute("value"), "Second output should be updated"
    finally:
        driver.quit()
        stop_server(process)


if __name__ == "__main__":
    test_text_updates()
    test_graph_updates()
    test_multiple_output_updates()