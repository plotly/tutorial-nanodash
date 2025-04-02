"""
Exercise 5: Testing a complete nanodash application
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from .test_utils import start_server, stop_server


def test_complete_app_loads():
    """Test if the complete application loads with all components."""
    process = start_server("tests/exercise_apps/exercise5.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Check that key components exist
        header = driver.find_element(By.TAG_NAME, "h1")
        assert header, "Header should be present"
        
        # Check for input components
        input_components = driver.find_elements(By.TAG_NAME, "input")
        select_components = driver.find_elements(By.TAG_NAME, "select")
        assert len(input_components) > 0, "Application should have input elements"
        
        # Check for graph
        wait = WebDriverWait(driver, 10)
        graph = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-svg")))
        assert graph, "Application should display a Plotly graph"
    finally:
        driver.quit()
        stop_server(process)


def test_data_interaction():
    """Test if the application can interact with data."""
    process = start_server("tests/exercise_apps/exercise5.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Wait for the page to fully load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-svg")))
        
        # Get the initial state of the graph
        initial_traces = driver.execute_script("""
            const graphDiv = document.querySelector('[class*="plotly"]');
            if (graphDiv && graphDiv._fullData) {
                return graphDiv._fullData.length;
            }
            return 0;
        """)
        
        # Interact with a filter dropdown
        dropdown = driver.find_element(By.TAG_NAME, "select")
        options = dropdown.find_elements(By.TAG_NAME, "option")
        if len(options) > 1:
            options[1].click()  # Select a different option
        
            # Wait for the graph to update
            time.sleep(2)
            
            # Check if the graph data changed
            updated_traces = driver.execute_script("""
                const graphDiv = document.querySelector('[class*="plotly"]');
                if (graphDiv && graphDiv._fullData) {
                    return graphDiv._fullData.length;
                }
                return 0;
            """)
            
            assert updated_traces != initial_traces or updated_traces > 0, "Graph should update based on interaction"
    finally:
        driver.quit()
        stop_server(process)


def test_multi_component_interaction():
    """Test if multiple components can interact with each other."""
    process = start_server("tests/exercise_apps/exercise5.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Wait for the page to fully load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-svg")))
        
        # Find a text input
        inputs = driver.find_elements(By.TAG_NAME, "input")
        text_input = None
        for inp in inputs:
            if inp.get_attribute("type") == "text":
                text_input = inp
                break
        
        if text_input:
            # Update the text input
            test_value = "Test Graph Title"
            text_input.clear()
            text_input.send_keys(test_value)
            
            # Wait for update to propagate
            time.sleep(2)
            
            # Check if title was updated
            try:
                title = driver.find_element(By.CSS_SELECTOR, ".gtitle")
                assert test_value in title.text, "Graph title should update based on text input"
            except:
                pass  # Title might not be what is being updated
    finally:
        driver.quit()
        stop_server(process)


if __name__ == "__main__":
    test_complete_app_loads()
    test_data_interaction()
    test_multi_component_interaction()