try:
    from nanodash.nanodash import NanoDash
    from nanodash.components import Header, TextInput, Graph, Page
except ModuleNotFoundError:
    from exercise6.nanodash import NanoDash
    from exercise6.nanodash.components import Header, TextInput, Graph, Page
import plotly.express as px
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 6: UI Updates from Callbacks")

# Create components for text update test
input_test = TextInput(id="input-test")
output_test = TextInput(id="output-test")

# Create components for graph update test
graph_input = TextInput(id="graph-input")

# Create an initial graph
fig = px.scatter(
    x=[1, 2, 3, 4, 5], 
    y=[1, 4, 9, 16, 25]
)

fig.update_layout(
    title="Initial Graph Title",
    xaxis=dict(title="X-Axis"),
    yaxis=dict(title="Y-Axis")
)

graph_test = Graph(
    id="graph-test",
    fig=fig
)

# Create components for multiple output test
multi_output_input = TextInput(id="multi-output-input")

output_1 = TextInput(id="output-1")
output_2 = TextInput(id="output-2")

# Create a page with all components
page = Page(children=[
    header,
    input_test,
    output_test,
    multi_output_input,
    output_1,
    output_2,
    graph_input,
    graph_test,
])

# Add layout to the app
app.set_layout(page)

# Add callbacks
def text_callback(inputs):
    """Echo the input text to the output."""
    return [inputs[0]]

app.add_callback(
    input_ids=["input-test"],
    output_ids=["output-test"],
    function=text_callback
)

def graph_update_callback(inputs):
    """Update the graph title based on input."""
    new_title = inputs[0]
    
    # Create a new figure with the updated title
    updated_fig = px.scatter(
        x=[1, 2, 3, 4, 5], 
        y=[1, 4, 9, 16, 25]
    )
    updated_fig.update_layout(
        title=new_title,
        xaxis=dict(title="X-Axis"),
        yaxis=dict(title="Y-Axis")
    )
    
    return [updated_fig]

app.add_callback(
    input_ids=["graph-input"],
    output_ids=["graph-test"],
    function=graph_update_callback
)

def multi_output_callback(inputs):
    """Update multiple outputs from a single input."""
    input_value = inputs[0]
    return [input_value, input_value]

app.add_callback(
    input_ids=["multi-output-input"],
    output_ids=["output-1", "output-2"],
    function=multi_output_callback
)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()