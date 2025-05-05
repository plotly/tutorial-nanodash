"""
Exercise 6: Testing UI updates from callback responses
"""

import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from exercise6.app import app
from test_utils import (
    start_app,
    set_component_value,
    get_component_value,
    get_graph_data,
    selenium_webdriver,
)


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return


def test_text_updates(selenium_webdriver):
    """Test if text outputs are updated correctly."""

    # Set values of the dropdowns and input
    new_year = "2022"
    new_month = "March"
    new_center_name = "All"
    new_chart_title = "Custom title"
    set_component_value(selenium_webdriver, "year-dropdown", new_year)
    set_component_value(selenium_webdriver, "month-dropdown", new_month)
    set_component_value(selenium_webdriver, "center-name-dropdown", new_center_name)
    set_component_value(selenium_webdriver, "chart-title-input", new_chart_title)

    # Wait for the callback to process and update the UI
    time.sleep(1)

    # Check if the output element was updated
    expected_message = (
        f"{new_year}, {new_month}, {new_center_name}, '{new_chart_title}'"
    )
    assert (
        get_component_value(selenium_webdriver, "output-message") == expected_message
    ), "Output should be updated to match input values"


def test_graph_updates(selenium_webdriver):
    """Test if graph components are updated correctly."""

    # Wait for Plotly graph to be initialized
    WebDriverWait(selenium_webdriver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#attendance-graph .main-svg"))
    )

    # Update some inputs that should trigger a graph update
    new_year = "2022"
    new_title = "Custom title"
    set_component_value(selenium_webdriver, "year-dropdown", new_year)
    set_component_value(selenium_webdriver, "chart-title-input", new_title)

    # Wait for the graph to update
    time.sleep(1)

    # Check if the graph title was updated
    title_element = selenium_webdriver.find_element(
        By.CSS_SELECTOR, "#attendance-graph .gtitle"
    )
    updated_title_in_layout = title_element.text
    assert updated_title_in_layout == new_title, (
        "Graph title should be updated to match input"
    )

    # Check if the graph data was updated to contain only data from 2022
    graph_data = get_graph_data(selenium_webdriver, "attendance-graph")
    print("graph_data: \n", graph_data)
    x_values = []
    for trace in graph_data:
        x_values.extend(trace["x"])
    x_values_as_datetimes = [datetime.fromisoformat(x) for x in x_values]
    assert all([x.year == int(new_year) for x in x_values_as_datetimes]), (
        f"Graph data should only contain data from {new_year}"
    )
