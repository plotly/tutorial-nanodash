try:
    from nanodash import NanoDash
    from nanodash.components import Dropdown, Header, Text, Page, TextInput
except ModuleNotFoundError:
    from exercise5.nanodash import NanoDash
    from exercise5.nanodash.components import Dropdown, Header, Text, Page, TextInput

# Create a new Flask web server
app = NanoDash(title="Exercise 5 test app")

# Create page layout
header = Header(text="Exercise 5: Running callbacks")
description1 = Text(
    text="This app tests whether the server can run callbacks and send a response containing the new values for the page components."
)
description2 = Text(
    text="Below, you'll find dropdowns to select a favorite color and animal, and a text input for your name. When you interact with the inputs, a request should be sent to the server with the new state, and the server should send a response containing the new text for the 'message' field. "
)
description3 = Text(
    text="You won't see the message field change on the page, because we haven't written the code to update the output components yet, but you can see the server's response in the 'Network' tab in your browser's developer tools."
)

input_label_1 = Text(text="Enter a name, and select a color and animal:")
name_input_1 = TextInput(
    id="name-textinput-1",
    value="",
)
color_dropdown_1 = Dropdown(
    id="color-dropdown-1",
    value="Blue",
    options=[
        "Red",
        "Blue",
        "Green",
        "Yellow",
        "Purple",
        "Orange",
        "Pink",
        "Brown",
        "Black",
        "White",
        "Gray",
        "Teal",
    ],
)
animal_dropdown_1 = Dropdown(
    id="animal-dropdown-1",
    value="Dog",
    options=[
        "Dog",
        "Cat",
        "Bird",
        "Horse",
        "Rabbit",
        "Turtle",
        "Hamster",
        "Elephant",
        "Lion",
        "Tiger",
        "Dolphin",
    ],
)
output_label_1 = Text(text="Output 1:")
textfield_output_1 = TextInput(
    id="textfield-output-1",
    value="",
)

divider_1 = Text(text="-------------")

input_label_2 = Text(text="Enter a name, and select a color and animal:")
name_input_2 = TextInput(
    id="name-textinput-2",
    value="",
)
color_dropdown_2 = Dropdown(
    id="color-dropdown-2",
    value="Red",
    options=[
        "Red",
        "Blue",
        "Green",
        "Yellow",
        "Purple",
        "Orange",
        "Pink",
        "Brown",
        "Black",
        "White",
        "Gray",
        "Teal",
    ],
)
animal_dropdown_2 = Dropdown(
    id="animal-dropdown-2",
    value="Cat",
    options=[
        "Dog",
        "Cat",
        "Bird",
        "Horse",
        "Rabbit",
        "Turtle",
        "Hamster",
        "Elephant",
        "Lion",
        "Tiger",
        "Dolphin",
    ],
)
output_label_2 = Text(text="Output 2:")
textfield_output_2 = TextInput(
    id="textfield-output-2",
    value="",
)

# Create the page layout with all components
page = Page(
    children=[
        header,
        description1,
        description2,
        description3,
        # First set
        input_label_1,
        name_input_1,
        color_dropdown_1,
        animal_dropdown_1,
        output_label_1,
        textfield_output_1,
        divider_1,
        # Second set
        input_label_2,
        name_input_2,
        color_dropdown_2,
        animal_dropdown_2,
        output_label_2,
        textfield_output_2,
    ]
)

# Add layout to the app
app.set_layout(page)


# Define a callback to update the text field with a simple message
def generate_message(inputs):
    name = inputs[0]
    color = inputs[1].lower()
    animal = inputs[2].lower()
    """Generate a simple message combining the three inputs."""
    return [f"{name} likes {color} {animal}s!"]


# Add callback for first set of components
app.add_callback(
    input_ids=["name-textinput-1", "color-dropdown-1", "animal-dropdown-1"],
    output_ids=["textfield-output-1"],
    function=generate_message,
)

# Add callback for second set of components (reusing the same function)
app.add_callback(
    input_ids=["name-textinput-2", "color-dropdown-2", "animal-dropdown-2"],
    output_ids=["textfield-output-2"],
    function=generate_message,
)

# Run the app
if __name__ == "__main__":
    app.run()
