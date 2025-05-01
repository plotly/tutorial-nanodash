"""
Exercise 2: Testing component implementation (TextInput and Dropdown)
"""
import time
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from exercise2.app import app
# from test_utils import start_app, check_component_exists, set_component_value


def start_app(app_object):
    """
    Start the Flask app using the given path to the app file.
    """
    app = app_object

    def run_app():
        app.run(threaded=True, use_reloader=False, port=5000)
        
    # Create a thread to run the app
    app_thread = threading.Thread(
        target=run_app,
        daemon=True,
    )
    app_thread.start()

    wait_sec = 5
    print(f"Started app thread, waiting {wait_sec} seconds...")
    # Wait for a short time to ensure the server is up
    time.sleep(wait_sec)
    print("App is up and running (probably)") 


# Function which runs once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    """Setup for the test module."""
    # Start the server before running tests
    print("Starting server...")
    start_app(app)
    print("Server started.")
    return

def test_text_input_component():
    """Test if the TextInput component is properly implemented and renders correctly."""
    
    if True:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")

        # Print full HTML of page accessed by selenium
        # print("\n\nPage source:")
        # print(driver.page_source)
        # print("\n\n")
        # Check component exists
        # assert check_component_exists(driver, "chart-title-input"), "Text input component should exist"
        
        # Check that the text input component has tag <input> and type='text'
        text_input = driver.find_element(By.ID, "chart-title-input")
        assert text_input.tag_name == "input", "TextInput should render as an input element"
        assert text_input.get_attribute("type") == "text", "TextInput should have type='text'"
    
        # Check if the value is set correctly
        assert text_input.get_attribute("value") == "Pittsburgh Community Center Attendance"

def test_dropdown_component():
    """Test if the Dropdown component is properly implemented and renders correctly."""
    # with app_test_context("exercise2/app.py") as driver:
    if True:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        # Check component exists
        assert check_component_exists(driver, "month-dropdown"), "Month dropdown should exist on page"
        
        # Find dropdown component
        dropdown = driver.find_element(By.ID, "month-dropdown")
        assert dropdown.tag_name == "select", "Dropdown should render as a <select> element"
        
        # Check if options are correctly rendered
        options = dropdown.find_elements(By.TAG_NAME, "option")
        assert len(options) == 13, "Dropdown should have 13 options (12 months + 'All')"
        
        # Get text of second option
        second_option = options[1].text
        assert second_option == "January", "Second option should be 'January'"
        
        # Test component functionality using our utility
        assert set_component_value(driver, "dropdown-test", second_option), "Should be able to select dropdown option"
        assert dropdown.get_attribute("value") == second_option, "Dropdown should update its value"
