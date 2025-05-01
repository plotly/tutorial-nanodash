import pandas as pd

try:
    from nanodash import NanoDash
    from nanodash.components import Dropdown, Header, Text, Page, TextInput
except ModuleNotFoundError:
    from exercise2.nanodash import NanoDash
    from exercise2.nanodash.components import Dropdown, Header, Text, Page, TextInput


# Read data
data = pd.read_csv("data/pgh_community_centers.csv")
data["date"] = pd.to_datetime(data["date"])

# Create a new Flask web server
app = NanoDash(title="Sample NanoDash App")



###################
# Create page layout
###################
header = Header(text="Pittsburgh Community Center Attendance")
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
    options = ["All"] + sorted(list(data["center_name"].unique())),
)
chart_title_input_label = Text(text="Customize chart title: ")
chart_title_input = TextInput(
    id="chart-title-input",
    value="Pittsburgh Community Center Attendance",
)
page = Page(
    children=[
        header,
        citation,
        dropdown_label,
        year_dropdown,
        month_dropdown,
        center_name_dropdown,
        chart_title_input_label,
        chart_title_input,
    ]
)
# Add layout to the app
app.set_layout(page)


# Run the app
if __name__ == "__main__":
    app.run()
