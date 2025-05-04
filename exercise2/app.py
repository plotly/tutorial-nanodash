try:
    from nanodash import NanoDash
    from nanodash.components import Dropdown, Header, Text, Page, TextInput
except ModuleNotFoundError:
    from exercise2.nanodash import NanoDash
    from exercise2.nanodash.components import Dropdown, Header, Text, Page, TextInput

# Create a new Flask web server
app = NanoDash(title="Exercise 2 test app")

# Create page layout
header = Header(text="Exercise 2: Dropdown and TextInput components")
description1 = Text(
    text="This app tests whether the Dropdown and TextInput components are implemented correctly. "
)
description2 = Text(
    text="Below, you should see a dropdown menu containing a list of animals, and a text input field. "
)

# Create components
animal_dropdown_label = Text(text="Choose an animal:")
animal_dropdown = Dropdown(
    id="animal-dropdown",
    value="Porcupine",
    options=[
        "Deer",
        "Bear",
        "Beaver",
        "Porcupine",
        "Squirrel",
        "Raccoon",
        "Fox",
    ],
)

animal_textinput_label = Text(text="Or, enter another animal here:")
animal_textinput = TextInput(
    id="animal-textinput",
    value="Your favorite animal",
)

# Create the page layout with all components
page = Page(
    children=[
        header,
        description1,
        description2,
        animal_dropdown_label,
        animal_dropdown,
        animal_textinput_label,
        animal_textinput,
    ]
)

# Add layout to the app
app.set_layout(page)

# Run the app
if __name__ == "__main__":
    app.run()
