from nanodash.nanodash import NanoDash
from nanodash.components import Component

# Create a new Flask web server
app = NanoDash(debug=True)

header = Component("h1", "Hello, world!")
header_wrapper = Component("div", [header])
input = Component("input", "", {"name": "input_sample"})
output = Component("input", "", {"name": "output_sample"})
button = Component("button", "Click me!")
simple_component = Component("div", [header_wrapper, input, button, output])
app.set_layout(simple_component)


def sample_callback(inputs):
    output = inputs[0] + "!"
    return [output]


app.add_callback(
    inputs=[("input_sample", "value")],
    outputs=[("output_sample", "value")],
    function=sample_callback,
)

app.run()
