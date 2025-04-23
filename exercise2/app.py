try:
    from nanodash import NanoDash
    from nanodash.components import Header, TextInput, Dropdown, Page
except ModuleNotFoundError:
    from exercise2.nanodash import NanoDash
    from exercise2.nanodash.components import Header, TextInput, Dropdown, Page

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 2: TextInput and Dropdown Components")

# Create the components needed for the test
text_input = TextInput(id="input-test", value="Test Value")

dropdown = Dropdown(
    id="dropdown-test",
    options=["Option 1", "Option 2", "Option 3"],
)

# Create a page with the components
page = Page(children=[
    header,
    text_input,
    dropdown
])

# Add layout to the app
app.set_layout(page)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()