"""
Exercise 7: Testing your own app
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from test_utils import start_server


def test_header_exists():
    """Test if the app contains a header."""
    start_server("exercise7/app.py")
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        
        # Find element with the tag <h1>
        try:
            header = driver.find_element(By.TAG_NAME, "h1")
        except NoSuchElementException:
            header = None
   
        assert header is not None, "Page should contain a Header element"
            
    finally:
        driver.quit()
