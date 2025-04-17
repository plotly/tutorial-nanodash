from exercise3.nanodash.nanodash import NanoDash
from exercise3.nanodash.components import Header, Graph, Page
import plotly.express as px

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 3: Graph Component and Plotly Integration")

# Create a simple scatter plot
fig = px.scatter(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25])

# Create the graph component
graph = Graph(
    id="graph-test",
    fig=fig  # Convert Plotly figure to dictionary format
)

# Create a page with the components
page = Page(children=[
    header,
    graph
])

# Add layout to the app
app.set_layout(page)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()