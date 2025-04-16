"""
Exercise 2: Testing component implementation (TextInput and Dropdown)
"""
from selenium.webdriver.common.by import By
import pytest
from ..test_utils import app_test_context, check_component_exists, set_component_value


def test_text_input_component():
    """Test if the TextInput component is properly implemented and renders correctly."""
    with app_test_context("tests/exercise_apps/exercise2.py") as driver:
        # Check component exists
        assert check_component_exists(driver, "input-test"), "Text input component should exist"
        
        # Find text input component
        text_input = driver.find_element(By.ID, "input-test")
        assert text_input.tag_name == "input", "TextInput should render as an input element"
        assert text_input.get_attribute("type") == "text", "TextInput should have type='text'"
        

def test_dropdown_component():
    """Test if the Dropdown component is properly implemented and renders correctly."""
    with app_test_context("tests/exercise_apps/exercise2.py") as driver:
        # Check component exists
        assert check_component_exists(driver, "dropdown-test"), "Dropdown component should exist"
        
        # Find dropdown component
        dropdown = driver.find_element(By.ID, "dropdown-test")
        assert dropdown.tag_name == "select", "Dropdown should render as a select element"
        
        # Check if options are correctly rendered
        options = dropdown.find_elements(By.TAG_NAME, "option")
        assert len(options) >= 2, "Dropdown should have at least 2 options"
        
        # Get option value from second option
        option_value = options[1].get_attribute("value") or options[1].text
        
        # Test component functionality using our utility
        assert set_component_value(driver, "dropdown-test", option_value), "Should be able to select dropdown option"
        assert dropdown.get_attribute("value") == option_value, "Dropdown should update its value"


if __name__ == "__main__":
    test_text_input_component()
    test_dropdown_component()