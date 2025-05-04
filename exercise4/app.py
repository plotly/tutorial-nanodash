try:
    from nanodash import NanoDash
    from nanodash.components import Dropdown, Header, Text, Page, TextInput
except ModuleNotFoundError:
    from exercise4.nanodash import NanoDash
    from exercise4.nanodash.components import Dropdown, Header, Text, Page, TextInput

# Create a new Flask web server
app = NanoDash(title="Exercise 4 test app")

# Create page layout
header = Header(text="Exercise 4: Client to server communication")
description1 = Text(
    text="This app tests whether the client can capture state and send it to the server."
)
description2 = Text(
    text="Below, you'll find dropdowns to select a playing card and a text input for your name. When you change the values, a request should be sent to the server with the new state. You can't see the request on the page, but you can see it in the 'Network' tab in your browser's developer tools."
)

# Create components with new IDs
suit_dropdown_label = Text(text="Select a card suit:")
suit_dropdown = Dropdown(
    id="card-suit",
    value="Hearts",
    options=[
        "Hearts",
        "Diamonds",
        "Clubs",
        "Spades",
    ],
)

rank_dropdown_label = Text(text="Select a card rank:")
rank_dropdown = Dropdown(
    id="card-rank",
    value="Ace",
    options=[
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ],
)

player_label = Text(text="Enter your name:")
player_input = TextInput(
    id="player-name",
    value="",
)

# Create the page layout with all components
page = Page(
    children=[
        header,
        description1,
        description2,
        suit_dropdown_label,
        suit_dropdown,
        rank_dropdown_label,
        rank_dropdown,
        player_label,
        player_input,
    ]
)

# Add layout to the app
app.set_layout(page)

# Run the app
if __name__ == "__main__":
    app.run()