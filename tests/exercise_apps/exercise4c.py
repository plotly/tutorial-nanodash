from nanodash.nanodash import NanoDash
from nanodash.components import Header, TextField, Graph, Page
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash(debug=True)

# Create a header component
header = Header(text="Exercise 4c: UI Updates from Callbacks")

# Create components for text update test
input_test = TextField(id="input-test")
output_test = TextField(id="output-test")

# Create components for graph update test
graph_input = TextField(id="graph-input")

# Create an initial graph
fig = go.Figure(
    data=[go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25], mode='markers+lines')],
    layout=go.Layout(
        title="Initial Graph Title",
        xaxis=dict(title="X-Axis"),
        yaxis=dict(title="Y-Axis")
    )
)

graph_test = Graph(
    id="graph-test",
    fig=fig
)

# Create components for multiple output test
multi_output_input = TextField(id="multi-output-input")

output_1 = TextField(id="output-1")
output_2 = TextField(id="output-2")

# Create a page with all components
page = Page(children=[
    header,
    input_test,
    output_test,
    graph_input,
    graph_test,
    multi_output_input,
    output_1,
    output_2
])

# Add layout to the app
app.set_layout(page)

# Add callbacks
def text_callback(inputs):
    """Echo the input text to the output."""
    return [inputs[0]]

app.add_callback(
    inputs=["input-test"],
    outputs=["output-test"],
    function=text_callback
)

def graph_update_callback(inputs):
    """Update the graph title based on input."""
    new_title = inputs[0]
    
    # Create a new figure with the updated title
    updated_fig = go.Figure(
        data=[go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25], mode='markers+lines')],
        layout=go.Layout(
            title=new_title,
            xaxis=dict(title="X-Axis"),
            yaxis=dict(title="Y-Axis")
        )
    )
    
    return [updated_fig]

app.add_callback(
    inputs=["graph-input"],
    outputs=["graph-test"],
    function=graph_update_callback
)

def multi_output_callback(inputs):
    """Update multiple outputs from a single input."""
    input_value = inputs[0]
    return [input_value, input_value]

app.add_callback(
    inputs=["multi-output-input"],
    outputs=["output-1", "output-2"],
    function=multi_output_callback
)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()