from nanodash.nanodash import NanoDash
from nanodash.components import Component

# Create a new Flask web server
app = NanoDash(debug=True)

header = Component('h1', 'Hello, world!')
header_wrapper = Component('div', [header])
input = Component('input', '', {'name': 'input_sample'})
button = Component('button', 'Click me!')
simple_component = Component('div', [header_wrapper, input, button])
app.set_layout(simple_component)

app.run()