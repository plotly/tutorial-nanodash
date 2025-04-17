"""
Exercise 1: Testing the basic Flask server with static HTML capabilities
"""
import requests
from selenium.webdriver.common.by import By
import pytest
from test_utils import start_server, app_test_context

def test_page_structure():
    """Test if the Flask server is running and returning HTML content."""
    server_thread = start_server("exercise1/app.py")
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200
    assert "<html" in response.text, "Response does not contain HTML"

    """Test if the base HTML structure is correct."""
    with app_test_context("exercise1/app.py") as driver:
        # Check for basic page elements
        assert driver.title, "Page should have a title"

        assert driver.find_element(By.TAG_NAME, "h1"), "Page should have an <h1> element"
        

