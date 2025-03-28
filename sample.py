from nanodash.nanodash import NanoDash
from nanodash.components import Dropdown, Header, TextField, Button, Slider, Page, Graph
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash(title="Sample NanoDash App")

# Create a header component
header = Header(text="Hello, world!")

###################
# COMPONENTS
###################
input = TextField(
    id="input-sample",
)
slider_output = TextField(id="slider-output")
dropdown_output = TextField(id="dropdown-output")
button = Button(text="Click me!")
slider = Slider(
    id="slider-sample",
    min=0,
    max=100,
    step=1,
)
dropdown = Dropdown(
    id="dropdown-sample",
    options=["Option 1", "Option 2", "Option 3"],
)
graph_component = Graph(
    fig={
        "data": [],
        "layout": {},
        "config": {},
    },
    id="graph-component-sample",
)
all_components = Page(
    children=[
        header,
        input,
        button,
        slider,
        slider_output,
        dropdown,
        dropdown_output,
        graph_component,
    ]
)

# Add layout to the app
app.set_layout(all_components)


###################
# CALLBACKS
###################
def slider_callback(input_values):
    return [input_values[0]]


app.add_callback(
    input_ids=["slider-sample"],
    output_ids=["slider-output"],
    function=slider_callback,
)


def dropdown_callback(input_values):
    return [input_values[0]]


app.add_callback(
    input_ids=["dropdown-sample"],
    output_ids=["dropdown-output"],
    function=dropdown_callback,
)


def sample_callback(input_values):
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[1, 2, 3]))
    fig.layout.title = input_values[0] + "!"
    return [fig]


app.add_callback(
    input_ids=["input-sample"],
    output_ids=["graph-component-sample"],
    function=sample_callback,
)

# Run the app
app.run()
