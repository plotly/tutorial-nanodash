import plotly.express as px
import pandas as pd

try:
    from nanodash import NanoDash
    from nanodash.components import Dropdown, Header, Text, Page, Graph, TextInput
except ModuleNotFoundError:
    from exercise6.nanodash import NanoDash
    from exercise6.nanodash.components import (
        Dropdown,
        Header,
        Text,
        Page,
        Graph,
        TextInput,
    )


# Read data
data = pd.read_csv("data/pgh_community_centers.csv")
data["date"] = pd.to_datetime(data["date"])

# Create a new Flask web server
app = NanoDash(title="Exercise 6 test app")


def make_graph(year, month, center_name, custom_title=""):
    # Show only data from selected year
    data_filtered = data[data["date"].dt.year == int(year)]
    # Show only data from selected month
    if month != "All":
        data_filtered = data_filtered[data_filtered["date"].dt.month_name() == month]
    # Show only data from selected center
    if center_name != "All":
        data_filtered = data_filtered[data_filtered["center_name"] == center_name]
    # Use custom title if provided, otherwise create title from inputs
    title = custom_title or make_chart_title(year, month, center_name)
    # Create the graph
    fig = px.bar(
        data_filtered,
        x="date",
        y="attendance_count",
        color="center_name",
        barmode="stack",
    )
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Attendance count",
        showlegend=False,
    )
    return fig


def make_chart_title(year, month, center_name):
    center_name = (
        center_name + " (Pittsburgh)"
        if center_name != "All"
        else "Pittsburgh community centers"
    )
    title = f"Daily attendance at {center_name}, "
    if month != "All":
        title += month + " "
    title += year
    return title


###################
# Create page layout
###################
header = Header(text="Exercise 6: Updating the page with callback results")
description1 = Text(
    text="This app tests whether the client can update the values of the components on the page after receiving a callback response from the server."
)
description2 = Text(
    text="This app is similar to the sample app. Below, you'll find dropdowns to select a year, month, and community center. When you change the values, a request should be sent to the server with the new state, the server should send a response containing the new graph, and the graph that you see below should be updated. In addition, the text field 'Selection summary' should be updated to show the values of the inputs."
)
graph = Graph(
    fig=make_graph(year="2025", month="All", center_name="All"),
    id="attendance-graph",
)
citation = Text(
    text="Data source: Western Pennsylvania Regional Data Center (data.wprdc.org)"
)
dropdown_label = Text(text="Filter data:")
year_dropdown = Dropdown(
    id="year-dropdown",
    value="2025",
    options=sorted([str(y) for y in data["date"].dt.year.unique()]),
)
month_dropdown = Dropdown(
    id="month-dropdown",
    value="April",
    options=[
        "All",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
)
center_name_dropdown = Dropdown(
    id="center-name-dropdown",
    value="All",
    options=["All"] + sorted(list(data["center_name"].unique())),
)
chart_title_input_label = Text(text="Customize chart title: ")
chart_title_input = TextInput(
    id="chart-title-input",
    value="Pittsburgh Community Center Attendance",
)

# Add output message component for test_text_updates
output_message_label = Text(text="Selection summary:")
output_message = TextInput(
    id="output-message",
    value="",
)

page = Page(
    children=[
        header,
        description1,
        description2,
        citation,
        dropdown_label,
        year_dropdown,
        month_dropdown,
        center_name_dropdown,
        chart_title_input_label,
        chart_title_input,
        output_message_label,
        output_message,
        graph,
    ]
)
# Add layout to the app
app.set_layout(page)


###################
# Add callbacks
###################


# First callback: update the graph
def update_graph(inputs):
    # Unpack inputs
    year = inputs[0]
    month = inputs[1]
    center_name = inputs[2]
    custom_title = inputs[3]

    # Generate graph
    fig = make_graph(
        year=year, month=month, center_name=center_name, custom_title=custom_title
    )
    return [fig]


# Second callback: update the message
def update_message(inputs):
    # Unpack inputs
    year = inputs[0]
    month = inputs[1]
    center_name = inputs[2]
    custom_title = inputs[3]

    # Generate message for the output-message component
    message = f"{year}, {month}, {center_name}, '{custom_title}'"
    return [message]


# Add both callbacks with the same inputs but different outputs
app.add_callback(
    input_ids=[
        "year-dropdown",
        "month-dropdown",
        "center-name-dropdown",
        "chart-title-input",
    ],
    output_ids=["attendance-graph"],
    function=update_graph,
)

app.add_callback(
    input_ids=[
        "year-dropdown",
        "month-dropdown",
        "center-name-dropdown",
        "chart-title-input",
    ],
    output_ids=["output-message"],
    function=update_message,
)

if __name__ == "__main__":
    # Run the app
    app.run()
