"""
Comprehensive test utilities for NanoDash tests

This module provides a unified set of utilities for testing NanoDash applications:
1. Server management: start_server
2. Test contexts: app_test_context
3. Component interaction: check_component_exists, set_component_value
4. Graph testing: wait_for_graph_render, get_graph_data
5. Network testing: setup_fetch_interceptor
"""
import threading
import time
import importlib.util
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contextlib import contextmanager


def start_server(script_path):
    """Start a Flask server using threading.
    
    Args:
        script_path: Path to the Flask application script
        
    Returns:
        Thread object running the server
    """
    # Load the app module
    spec = importlib.util.spec_from_file_location("app_module", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["app_module"] = module
    spec.loader.exec_module(module)
    
    # Assuming the Flask app is named 'app' in the module
    app = module.app
    
    # Create a thread to run the server
    server_thread = threading.Thread(
        target=lambda: app.run()
    )
    server_thread.daemon = True
    server_thread.start()
    
    # Give the server time to start
    time.sleep(2)
    
    return server_thread


@contextmanager
def app_test_context(script_path):
    """Context manager for running tests with server and browser.
    
    Args:
        script_path: Path to the Flask application script
        
    Yields:
        Selenium WebDriver instance connected to the running app
        
    Usage:
        with app_test_context("path/to/app.py") as driver:
            # Test with the browser
    """
    server_thread = start_server(script_path)
    driver = webdriver.Chrome()
    try:
        driver.get("http://127.0.0.1:5000")
        yield driver
    finally:
        driver.quit()
        # Server stops automatically as it's a daemon thread


def wait_for_graph_render(driver, graph_id="#graph-test", timeout=10):
    """Wait for a Plotly graph to render and return the SVG element.
    
    Args:
        driver: Selenium WebDriver instance
        graph_id: ID of the graph component (with or without # prefix)
        timeout: Maximum time to wait in seconds
        
    Returns:
        The SVG element if graph rendered within timeout
        
    Raises:
        TimeoutException if graph does not render within timeout
    """
    # Ensure graph_id starts with #
    if not graph_id.startswith('#'):
        graph_id = f"#{graph_id}"
        
    wait = WebDriverWait(driver, timeout)
    return wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"{graph_id} .main-svg"))
    )


def setup_fetch_interceptor(driver, url_path='/state'):
    """Setup JavaScript to intercept fetch requests and store payloads/responses.
    
    Args:
        driver: Selenium WebDriver instance
        url_path: URL path to intercept (default: '/state')
    """
    driver.execute_script(f"""
        window.lastPayload = null;
        window.lastResponse = null;
        const originalFetch = window.fetch;
        window.fetch = function(url, options) {{
            if (url === '{url_path}' && options && options.body) {{
                window.lastPayload = JSON.parse(options.body);
            }}
            return originalFetch(url, options).then(response => {{
                if (url === '{url_path}') {{
                    return response.clone().json().then(data => {{
                        window.lastResponse = data;
                        return response;
                    }});
                }}
                return response;
            }});
        }};
    """)


def check_component_exists(driver, component_id):
    """Check if a component exists in the DOM.
    
    Args:
        driver: Selenium WebDriver instance
        component_id: ID of the component to check
        
    Returns:
        True if the component exists, False otherwise
    """
    try:
        driver.find_element(By.ID, component_id)
        return True
    except:
        return False


def get_graph_data(driver, graph_id):
    """Get the data from a Plotly graph.
    
    Args:
        driver: Selenium WebDriver instance
        graph_id: ID of the graph component
        
    Returns:
        Dictionary with graph data or None if not found
    """
    return driver.execute_script(f"""
        const graphDiv = document.getElementById('{graph_id}');
        if (graphDiv && graphDiv._fullData) {{
            return {{
                traces: graphDiv._fullData.length,
                title: graphDiv.layout.title ? graphDiv.layout.title.text : '',
                hasData: graphDiv._fullData.some(trace => trace.x && trace.x.length > 0)
            }};
        }}
        return null;
    """)


def set_component_value(driver, component_id, value):
    """Set the value of a component.
    
    Args:
        driver: Selenium WebDriver instance
        component_id: ID of the component
        value: Value to set
        
    Returns:
        True if successful, False otherwise
    """
    try:
        element = driver.find_element(By.ID, component_id)
        element_type = element.tag_name.lower()
        
        if element_type == "input":
            input_type = element.get_attribute("type")
            if input_type == "text":
                element.clear()
                element.send_keys(value)
            elif input_type == "range":
                driver.execute_script(f"document.getElementById('{component_id}').value = {value};")
                driver.execute_script(f"document.getElementById('{component_id}').dispatchEvent(new Event('input'));")
        elif element_type == "select":
            options = element.find_elements(By.TAG_NAME, "option")
            for option in options:
                if option.text == value or option.get_attribute("value") == value:
                    option.click()
                    break
        
        return True
    except:
        return False


def get_component_value(driver, component_id):
    """Get the value of a component.
    
    Args:
        driver: Selenium WebDriver instance
        component_id: ID of the component
        
    Returns:
        Value of the component or None if component doesn't exist
    """
    try:
        element = driver.find_element(By.ID, component_id)
        element_type = element.tag_name.lower()
        
        if element_type == "input":
            return element.get_attribute("value")
        elif element_type == "select":
            return element.get_attribute("value")
        elif element_type == "div":
            # For components that might store their value in innerHTML
            return element.text
            
        return None
    except:
        return None


def wait_for_callback_completion(driver, timeout=5):
    """Wait for all pending callbacks to complete.
    
    Args:
        driver: Selenium WebDriver instance
        timeout: Maximum time to wait in seconds
        
    Returns:
        True if callbacks completed within timeout, False otherwise
    """
    try:
        start_time = time.time()
        while time.time() - start_time < timeout:
            # Check if the fetch interceptor has recorded a response
            has_response = driver.execute_script("return window.lastResponse !== null;")
            if has_response:
                # Give a small additional time for UI updates
                time.sleep(0.5)
                return True
            time.sleep(0.1)
        return False
    except:
        return False