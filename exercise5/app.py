try:
    from nanodash import NanoDash
    from nanodash.components import Header, TextField, Dropdown, Page
except ModuleNotFoundError:
    from exercise5.nanodash import NanoDash
    from exercise5.nanodash.components import Header, TextField, Dropdown, Page

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 5: Server-to-Client Communication")

# Create input components
text_input = TextField(id="input-test")

dropdown = Dropdown(
    id="dropdown-test",
    options=["Option 1", "Option 2", "Option 3"],
)

# Create output components
text_output = TextField(id="output-test")

dropdown_output = TextField(id="dropdown-output")

# Create a page with the components
page = Page(children=[
    header,
    text_input,
    text_output,
    dropdown,
    dropdown_output
])

# Add layout to the app
app.set_layout(page)

# Add callbacks
def text_callback(inputs):
    """Simple echo callback for text input."""
    return [inputs[0]]

app.add_callback(
    input_ids=["input-test"],
    output_ids=["output-test"],
    function=text_callback
)

def dropdown_callback(inputs):
    """Echo callback for dropdown selection."""
    return [inputs[0]]

app.add_callback(
    input_ids=["dropdown-test"],
    output_ids=["dropdown-output"],
    function=dropdown_callback
)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()