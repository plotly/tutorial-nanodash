import time
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_callback(sample_app, start_app):
    # Start the app in another thread
    start_app(sample_app)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:5000")

    # Set text in the input with id "input_sample"
    driver.find_element(By.ID, "input_sample").send_keys("Hello, world!")

    time.sleep(2)

    # Check that it is showing up as the graph title
    graph = driver.find_element(By.ID, "graph-component-sample").find_element(
        By.CLASS_NAME, "g-gtitle"
    )
    assert graph.text == "Hello, world!!"

    # Close the driver
    driver.quit()
