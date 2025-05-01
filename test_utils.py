"""
This module provides a set of utilities for testing NanoDash applications
"""
import threading
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.fixture
def selenium_webdriver():
    """
    Pytest fixture for launching and quitting a Selenium WebDriver instance. 
    
    Yields:
        Selenium WebDriver instance connected to the running app
        
    Usage:
        text_input = selenium_webdriver.find_element(By.ID, "element-id")
    """
    driver = None
    try:
        driver = create_webdriver()
        yield driver
    except Exception as e:
        raise e
    finally:
        if driver:
            driver.quit()


def create_webdriver(headless: bool=False):
    """
    Returns a new Selenium WebDriver instance pointed at 127.0.0.1:5000.
    
    Args:
        headless: If True, run the browser in headless mode (no GUI).
        
    Returns:
        Selenium WebDriver instance
    """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:5000")
    return driver


def start_app(app_object):
    """
    Start the provided Flask app in a daemon thread.
    """
    app = app_object

    def run_app():
        app.run(threaded=True, use_reloader=False, port=5000)
        
    app_thread = threading.Thread(
        target=run_app,
        daemon=True,
    )
    app_thread.start()

    # Wait for the app to start
    driver = create_webdriver(headless=True)
    WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.TAG_NAME, "html"))
    )
    driver.quit()
    return app_thread


def wait_for_graph_render(driver, graph_id, timeout=10):
    """Wait for a Plotly graph to render and return the SVG element.

    Args:
        driver: Selenium WebDriver instance
        graph_id: ID of the graph component to wait for
        timeout: Maximum time to wait in seconds

    Returns:
        True if graph rendered within timeout, False otherwise
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"#{graph_id} .main-svg"))
        )
        return True
    except TimeoutException:
        return False


def setup_fetch_interceptor(driver, url_path='/handle-change'):
    """Setup JavaScript to intercept fetch requests and store payloads/responses.
    
    Args:
        driver: Selenium WebDriver instance
        url_path: URL path to intercept (default: '/handle-change')
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
    except NoSuchElementException:
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
        if (graphDiv && graphDiv.data) {{
            return graphDiv.data;
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