from nanodash.nanodash import NanoDash
from nanodash.components import Header, TextField, Dropdown, Graph, Page, Slider
import plotly.express as px
import numpy as np

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 5: Complete NanoDash Application")

# Create input components
title_input = TextField(
    id="title-input",
    value="Sample Dashboard"
)

# Create data selector dropdown
data_type_dropdown = Dropdown(
    id="data-type-dropdown",
    options=["Scatter Plot", "Bar Chart", "Line Chart"],
    value="Scatter Plot"
)

# Create a points slider
points_slider = Slider(
    id="points-slider",
    min=5,
    max=50,
    step=5,
    value=20
)

# Create a simple scatter plot
initial_points = 20
x = np.linspace(0, 10, initial_points)
y = np.sin(x)

fig = px.scatter(x=x, y=y, mode='markers')

graph = Graph(
    id="main-graph",
    fig=fig
)

# Create a page with all components
page = Page(children=[
    header,
    title_input,
    data_type_dropdown,
    points_slider,
    graph
])

# Add layout to the app
app.set_layout(page)

# Add callbacks
def update_graph_title(inputs):
    """Update the graph title based on input."""
    title = inputs[0]
    
    fig = go.Figure(
        layout=go.Layout(
            title=title
        )
    )
    
    return [fig]

app.add_callback(
    inputs=["title-input"],
    outputs=["main-graph"],
    function=update_graph_title
)

def update_graph_type(inputs):
    """Update the graph type based on dropdown selection."""
    graph_type = inputs[0]
    num_points = int(inputs[1])
    
    x = np.linspace(0, 10, num_points)
    y = np.sin(x)
    
    if graph_type == "Bar Chart":
        fig = go.Figure(data=[go.Bar(x=x, y=y)])
    elif graph_type == "Line Chart":
        fig = go.Figure(data=[go.Scatter(x=x, y=y, mode="lines")])
    else:  # Default to Scatter Plot
        fig = go.Figure(data=[go.Scatter(x=x, y=y, mode="markers")])
    
    # Maintain the title from the title input
    title = inputs[2] if len(inputs) > 2 else "Sample Dashboard"
    fig.update_layout(
        title=title,
        xaxis=dict(title="X Values"),
        yaxis=dict(title="Y Values")
    )
    
    return [fig]

app.add_callback(
    inputs=["data-type-dropdown", "points-slider", "title-input"],
    outputs=["main-graph"],
    function=update_graph_type
)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()