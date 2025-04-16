from nanodash.nanodash import NanoDash
from nanodash.components import Dropdown, Header, Text, Page, Graph
import plotly.express as px
import pandas as pd

# Read data
data = pd.read_csv("sample-apps/community-centers/data.csv")
data["date"] = pd.to_datetime(data["date"])

# Create a new Flask web server
app = NanoDash(title="Sample NanoDash App")


def make_graph(year, month, center_name):
    # Show only data from selected year
    data_filtered = data[data["date"].dt.year == int(year)]
    # Show only data from selected month
    if month != "All":
        data_filtered = data_filtered[data_filtered["date"].dt.month_name() == month]
    # Show only data from selected center
    if center_name != "All":
        data_filtered = data_filtered[data_filtered["center_name"] == center_name]
    # Create the graph
    fig = px.bar(
        data_filtered,
        x="date",
        y="attendance_count",
        color="center_name",
        barmode="stack",
    )
    fig.update_layout(
        title="Daily attendance at Pittsburgh community centers",
        xaxis_title="Date",
        yaxis_title="Attendance count",
        showlegend=False,
    )
    return fig


###################
# Create page layout
###################
header = Header(text="Pittsburgh Community Center Attendance")
graph = Graph(
    fig=make_graph(year="2025", month="All", center_name="All"),
    id="attendance-graph",
)
citation = Text(
    text="Source: Western Pennsylvania Regional Data Center (data.wprdc.org)"
)
unique_years = [str(y) for y in data["date"].dt.year.unique()]
year_dropdown = Dropdown(
    id="year-dropdown",
    options=unique_years,
    # value="2025",
)
unique_months = [
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
]
month_dropdown = Dropdown(
    id="month-dropdown",
    options=unique_months,
    # value="March",
)
unique_centers = ["All"] + list(data["center_name"].unique())
center_name_dropdown = Dropdown(
    id="center-name-dropdown",
    options=unique_centers,
    # value="All",
)
page = Page(
    children=[
        header,
        citation,
        year_dropdown,
        month_dropdown,
        center_name_dropdown,
        graph,
    ]
)
# Add layout to the app
app.set_layout(page)


###################
# Add callbacks
###################
def update_graph(inputs):
    # Unpack inputs
    year = inputs[0]
    month = inputs[1]
    center_name = inputs[2]
    fig = make_graph(year=year, month=month, center_name=center_name)
    return [fig]


app.add_callback(
    input_ids=["year-dropdown", "month-dropdown", "center-name-dropdown"],
    output_ids=["attendance-graph"],
    function=update_graph,
)

# Run the app
app.run()
