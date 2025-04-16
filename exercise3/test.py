"""
Exercise 3: Testing the Graph component and Plotly integration
"""
from selenium.webdriver.common.by import By
import pytest
from .test_utils import app_test_context, wait_for_graph_render, check_component_exists, get_graph_data


def test_graph_component_rendered():
    """Test if the Graph component is rendered correctly."""
    with app_test_context("tests/exercise_apps/exercise3.py") as driver:
        # Check that the graph container exists
        assert check_component_exists(driver, "graph-test"), "Graph container should be present"
        
        # Check that Plotly is rendering the graph (look for SVG elements)
        svg_element = wait_for_graph_render(driver)
        assert svg_element, "Plotly should render an SVG graph"
        
        # Verify plotly traces are present
        traces = driver.find_elements(By.CSS_SELECTOR, ".scatter")
        assert len(traces) > 0, "Plotly graph should contain trace elements"


def test_graph_components_present():
    """Test if the Graph component has the expected Plotly structure."""
    with app_test_context("tests/exercise_apps/exercise3.py") as driver:
        # Wait for Plotly to render the graph
        wait_for_graph_render(driver)
        
        # Get graph data using our utility
        graph_data = get_graph_data(driver, "graph-test")
        assert graph_data, "Should be able to access graph data"
        assert graph_data['traces'] > 0, "Graph should have at least one trace"
        assert graph_data['hasData'], "Graph traces should contain data"
        
        # Check for axes
        x_axis = driver.find_elements(By.CSS_SELECTOR, ".xaxislayer-above")
        y_axis = driver.find_elements(By.CSS_SELECTOR, ".yaxislayer-above")
        assert x_axis, "X-axis should be rendered"
        assert y_axis, "Y-axis should be rendered"


if __name__ == "__main__":
    test_graph_component_rendered()
    test_graph_components_present()