from nanodash.nanodash import NanoDash
from nanodash.components import Component, Graph
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash(debug=True)

header = Component("h1", "Hello, world!")
header_wrapper = Component("div", [header])
input = Component("input", "", {"name": "input_sample"})
output = Component("input", "", {"name": "output_sample"})
button = Component("button", "Click me!")
slider = Component("input", "", {"name": "slider_sample", "type": "range", "min": 0, "max": 100, "step": 1})
graph_component = Graph(graph_obj={"data": [], "layout": {}, "config": {}}, attributes={"name": "graph-component-sample", "id": "graph-component-sample"})
simple_component = Component("div", [header_wrapper, input, button, slider, output, graph_component])

app.set_layout(simple_component)

def slider_callback(inputs):
    return [inputs[0]]

app.add_callback(
    inputs=[("slider_sample", "value")],
    outputs=[("output_sample", "value")],
    function=slider_callback,
)

def sample_callback(inputs):
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[1, 2, 3]))
    fig.layout.title = inputs[0] + "!"
    return [fig]


app.add_callback(
    inputs=[("input_sample", "value")],
    outputs=[("graph-component-sample", "value")],
    function=sample_callback,
)

app.run()
