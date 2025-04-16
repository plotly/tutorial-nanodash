from nanodash.nanodash import NanoDash
from nanodash.components import Header, Page

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="Exercise 1: Basic Flask Server")

# Create a simple page with just a header
page = Page(children=[header])

# Add layout to the app
app.set_layout(page)

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()