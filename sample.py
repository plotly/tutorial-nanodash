from nanodash.nanodash import NanoDash
from nanodash.components import Component
from nanodash.graph import Graph
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash(debug=True)

# Create a header component
header = Header(
    children="Hello, world!"
)

###################
# COMPONENTS
###################
input = TextField(
    id="input_sample",
)
output = TextField(
    id="output_sample"
)
button = Button(
    children="Click me!"
)
slider = Slider(
    id="slider_sample", 
    type="range", 
    min=0, 
    max=100, 
    step=1,
)
graph_component = Graph(
    fig={
        "data": [],
        "layout": {}, 
        "config": {}
    }, 
    id="graph-component-sample"
)
all_components = Page(
    children = [
        header, 
        input, 
        button, 
        slider, 
        output, 
        graph_component
    ]
)

# Add layout to the app
app.set_layout(all_components)

###################
# CALLBACKS
###################
def slider_callback(inputs):
    return [inputs[0]]

app.add_callback(
    inputs=["slider_sample.value"],
    outputs=["output_sample.value"],
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

# Run the app
app.run()
