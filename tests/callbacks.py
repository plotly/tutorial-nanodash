from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_callback():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")

    # Set text in the input with id "input_sample"
    driver.find_element(By.ID, "input_sample").send_keys("Hello, world!")

    time.sleep(1)

    # Check that it is showing up as the graph title
    graph = driver.find_element(By.ID, "graph-component-sample").find_element(By.CLASS_NAME, "g-gtitle")
    assert graph.text == "Hello, world!!"

    # Close the driver
    driver.quit()