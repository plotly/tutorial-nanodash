from nanodash.nanodash import NanoDash
from nanodash.components import Header, Graph, Page
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 3: Graph Component and Plotly Integration")

# Create a simple scatter plot
fig = go.Figure(
    data=[go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25], mode='markers+lines')],
    layout=go.Layout(
        title="Sample Scatter Plot",
        xaxis=dict(title="X-Axis"),
        yaxis=dict(title="Y-Axis")
    )
)

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