from nanodash.nanodash import NanoDash
from nanodash.components import Component

# Create a new Flask web server
app = NanoDash(debug=True)

simple_component = Component('button', 'Emily rocks!')
app.set_layout(simple_component)

app.run()