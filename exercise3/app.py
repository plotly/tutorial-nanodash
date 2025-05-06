import plotly.express as px
import pandas as pd

try:
    from nanodash import NanoDash
    from nanodash.components import Dropdown, Header, Text, Page, Graph
except ModuleNotFoundError:
    from exercise3.nanodash import NanoDash
    from exercise3.nanodash.components import Dropdown, Header, Text, Page, Graph

# Create a new Flask web server
app = NanoDash(title="Exercise 3 test app")

# Create sample data for planets
planets_data = pd.DataFrame(
    {
        "planet": [
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune",
        ],
        "diameter_km": [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528],
    }
)


# Create a simple bar chart
def create_planets_chart():
    fig = px.bar(
        planets_data,
        x="planet",
        y="diameter_km",
        color="planet",
        title="Diameter of planets in our solar system",
    )
    fig.update_layout(
        xaxis_title="Planet", yaxis_title="Diameter (km)", showlegend=False
    )
    return fig


# Create page elements
header = Header(text="Exercise 3: Graph component")
description = Text(
    text="This app tests whether the Graph component is implemented correctly."
)
explanation = Text(
    text="Below, you should see a bar chart showing the diameters of planets in our solar system."
)

# Create the graph
planet_graph = Graph(id="planet-graph", fig=create_planets_chart())

citation = Text(text="Data source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/")

# Create the page layout with all components
page = Page(
    children=[
        header,
        description,
        explanation,
        planet_graph,
        citation,
    ]
)

# Add layout to the app
app.set_layout(page)

# Run the app
if __name__ == "__main__":
    app.run()
