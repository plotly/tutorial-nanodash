"""
This file contains the definition for the NanoDash class itself,
including logic for running the Flask server, returning the HTML layout
of the app, and handling callbacks.
"""

from typing import List

import flask
import plotly.graph_objects as go

from .components import Component


class NanoDash:
    def __init__(self, title: str = "NanoDash App") -> None:
        self.app = flask.Flask(__name__)
        self.title = title
        self.callbacks = []

        # This route is used to serve the main HTML page
        @self.app.route("/")
        def html() -> str:
            """
            Receives a request from the browser and returns the HTML
            for the main page.
            """
            return self.full_html()

        # This route is used to handle callbacks, convert application/json content-type to dict
        @self.app.route("/handle-change", methods=["POST"])
        def handle_change():
            """
            Receives a request from the frontend containing the current values of the
            app's components, and the id of the component that triggered the change.

            It then calls the appropriate callback functions and returns the new values
            for the components which should be updated.

            ==============
            Request format
            ==============
            {
                "state": {
                    "component-id-1": "component-value-1",
                    "component-id-2": "component-value-2",
                    ...
                },
                "trigger_id": "id-of-component-that-triggered-change"
            }

            ===============
            Response format
            ===============
            {
                "component-id-1": "updated-component-value-1",
                "component-id-2": "updated-component-value-2",
                ...
            }
            """

            # Construct the response
            response = {}

            print("Request received:")
            print(flask.request.json)

            # Send the response back to the frontend
            return response

    def set_layout(self, layout: Component) -> None:
        self.layout = layout

    def full_html(self) -> str:
        """
        Returns a string containing the full HTML for the home page
        of the app.

        For exercise 1, this function should return a simple hard-coded
        HTML page with a title and a body.

        In following exercises we will modify this function to return
        HTML matching the app's layout.

        For example, a very simple HTML page could look like this:
        '''
        <html>
            <head>
                <title>My webpage</title>
            </head>
            <body>
                <h1>Hello, world!</h1>
                <p>This is my HTML page.</p>
            </body>
        </html>
        '''
        """
        ## EXERCISE 1 START
        return f"""
        <html>
            <head>
                <script src="https://cdn.plot.ly/plotly-3.0.1.min.js" charset="utf-8"></script>
                <script src='static/utils.js'></script>
                <script src='static/index.js'></script>
                <title>{self.title}</title>
            </head>
            <body>
            {self.layout.html()}
            </body>
        </html>
        """
        ## EXERCISE 1 END

    def run(self, debug=True, **kwargs) -> None:
        """
        Run the NanoDash application by starting the Flask server.
        """
        self.app.run(debug=debug, **kwargs)
