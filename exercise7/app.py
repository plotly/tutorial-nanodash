from nanodash import NanoDash
from nanodash.components import Header, TextField, Graph, Page
import plotly.express as px
import plotly.graph_objects as go

# Create a new Flask web server
app = NanoDash()

# Create a header component
header = Header(text="This is a NanoDash app")

# Create a page with all components
page = Page(children=[
    header,
])

# Add layout to the app
app.set_layout(page)

# Add callbacks following this example:
# def my_callback(inputs):
#     """Echo the input text to the output."""
#     return [inputs[0]]
# app.add_callback(
#     input_ids=["input-id-1"],
#     output_ids=["output-id-1"],
#     function=my_callback
# )

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()