from exercise4.nanodash.nanodash import NanoDash
from exercise4.nanodash.components import Header, TextField, Dropdown, Page

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 4: Client-to-Server Communication")

# Create the components needed for the test
text_input = TextField(id="input-test")

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