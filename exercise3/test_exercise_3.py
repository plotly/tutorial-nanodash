"""
Exercise 3: Testing the Graph component and Plotly integration
"""

from selenium.webdriver.common.by import By
import pytest

from exercise3.app import app
from test_utils import (
    start_app,
    wait_for_graph_render,
    check_component_exists,
    get_graph_data,
    selenium_webdriver,
)


# Set up the tests by launching the test app in another thread
# Will run once at the start of the test file
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    start_app(app)
    return


def test_graph_component_present(selenium_webdriver):
    """Test that the Graph component is correctly implemented and present on the page."""

    # Check that the graph container exists
    assert check_component_exists(selenium_webdriver, "planet-graph"), (
        "Graph container should be present"
    )

    # Check that visual elements are rendered in the graph
    svg_element = wait_for_graph_render(selenium_webdriver, "planet-graph")
    assert svg_element, "Graph container should contain visual elements"

    # Check that X and Y axes are present in the graph
    assert selenium_webdriver.find_elements(By.CSS_SELECTOR, ".xaxislayer-above"), (
        "X-axis should be rendered"
    )
    assert selenium_webdriver.find_elements(By.CSS_SELECTOR, ".yaxislayer-above"), (
        "Y-axis should be rendered"
    )

    # Check that bars are present in graph
    bars = selenium_webdriver.find_elements(By.CSS_SELECTOR, ".bars")
    assert len(bars) > 0, "Graph container should contain bars (since it's a bar graph)"


def test_graph_component_contents(selenium_webdriver):
    """Test that the Graph component contains data in the expected Plotly format."""

    # Wait for Plotly to render the graph
    wait_for_graph_render(selenium_webdriver, "planet-graph")

    # Get graph data
    graph_data = get_graph_data(selenium_webdriver, "planet-graph")
    assert graph_data is not None, "Should be able to access graph data"
    assert len(graph_data) > 0, "Graph should have at least one trace"
    assert all([len(t["x"]) for t in graph_data]), "Graph traces should contain data"
