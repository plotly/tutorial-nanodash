"""
Exercise 2: Testing component implementation (TextInput and Dropdown)
"""

from selenium.webdriver.common.by import By
import pytest

from exercise2.app import app
from test_utils import (
    start_app,
    check_component_exists,
    set_component_value,
    selenium_webdriver,
)


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return


def test_dropdown_component(selenium_webdriver):
    """Test that the Dropdown component is correctly implemented."""

    # Check that the Dropdown component exists
    assert check_component_exists(selenium_webdriver, "animal-dropdown"), (
        "Dropdown should exist on page"
    )

    # Check that the Dropdown component has tag <select> and contains the correct options
    dropdown = selenium_webdriver.find_element(By.ID, "animal-dropdown")
    assert dropdown.tag_name == "select", "Dropdown should render as a <select> element"
    options = dropdown.find_elements(By.TAG_NAME, "option")
    assert len(options) == 7, "Dropdown should have 7 options"
    second_option = options[1].text
    assert second_option == "Bear", "Second option should be 'Bear'"

    # Check that the Dropdown component has the correct initial value
    assert dropdown.get_attribute("value") == "Porcupine", (
        "Dropdown should have initial value 'Porcupine'"
    )

    # Test whether we can set the value of the Dropdown component
    assert set_component_value(selenium_webdriver, "animal-dropdown", second_option), (
        "Should be able to select a Dropdown option"
    )
    assert dropdown.get_attribute("value") == second_option, (
        "Dropdown value should update after selecting a new value"
    )


def test_text_input_component(selenium_webdriver):
    """Test that the TextInput component is correctly implemented."""

    # Check that the TextInput component exists
    assert check_component_exists(selenium_webdriver, "animal-textinput"), (
        "Text input should exist on page"
    )

    # Check that the TextInput component has tag <input> and type='text'
    text_input = selenium_webdriver.find_element(By.ID, "animal-textinput")
    assert text_input.tag_name == "input", "TextInput should render as an input element"
    assert text_input.get_attribute("type") == "text", (
        "TextInput should have type='text'"
    )

    # Check that the TextInput component has the correct initial value
    assert text_input.get_attribute("value") == "Your favorite animal", (
        "TextInput should have initial value 'Your favorite animal'"
    )

    # Test whether we can set the value of the TextInput component
    new_text = "New text"
    assert set_component_value(selenium_webdriver, "animal-textinput", new_text), (
        "Should be able to set TextInput value"
    )
    assert text_input.get_attribute("value") == new_text, (
        "TextInput value should update after setting a new value"
    )
