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

            ====================
            Callback definitions
            ====================
            A callback is defined by 3 pieces of information:
            1. The IDs of the input components that trigger the callback
                when their value changes. These are given as a list of
                strings. The values of these components will be passed
                as a list to the callback function.
            2. The IDs of the output components that should be updated
                when the callback is triggered. These are given as a list of
                strings. The updated values of these components will be returned
                as a list by the callback function.
            3. The function that should be called when the callback is
                triggered. This function should take a list of input values
                as its argument (which aligns with the list of input IDs) and
                return a list of output values (which aligns with the list
                of output IDs).

            The app's callbacks are stored in the following format:
                self.callbacks = [
                    {
                        "input_ids": ["id-1", "id-2", ...],
                        "output_ids": ["id-3", "id-4", ...],
                        "function": <function-ref>,
                    },
                    ...
                ]
            """

            # Construct the response
            response = {}

            # Get the state and trigger_id from the request
            state = flask.request.json["state"]
            trigger_id = flask.request.json["trigger_id"]

            for callback in self.callbacks:
                # For each callback: Check if any of the callback's input_ids
                # matches the `trigger_id`` from the response
                # If yes:
                #  1. Retrieve the values of the callback inputs from the response's `state`
                #  2. Execute the callback function by passing the input values as a list, and get the output values
                #  3. Convert the output values to JSON-serializable format. You can use the helper function
                #     `make_json_serializable()`, which accepts a list and returns a list, to do this.
                #      This function will convert any Plotly figures in the output to JSON format.
                #  4. Add the output values to the response dict as key: value pairs, where the key is the output ID
                #     and the value is the output value returned from the callback

                ## EXERCISE 5 START
                pass
                ## EXERCISE 5 END

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

    def add_callback(
        self, input_ids: List[str], output_ids: List[str], function: callable
    ) -> None:
        """
        Adds a callback to the app.

        The add_callback() method doesn't handle the actual callback logic
        of figuring out which callbacks to trigger and when. It simply
        stores the callback information in the app's callbacks list. The
        actual logic for executing the callbacks is handled in the
        handle_change() method, which is called when a request is received
        from the browser.
        """
        self.callbacks.append(
            {"input_ids": input_ids, "output_ids": output_ids, "function": function}
        )

    def run(self, debug=True, **kwargs) -> None:
        """
        Run the NanoDash application by starting the Flask server.
        """
        self.app.run(debug=debug, **kwargs)


def make_json_serializable(output_values: List) -> List:
    """
    Helper function which converts any Plotly figures in the output values to JSON format.
    This is necessary because Plotly figures are Python objects, and they need to be converted
    to strings in a very particular way so that they can be sent between the server and the browser.
    """
    for index, output_value in enumerate(output_values):
        if isinstance(output_value, go.Figure):
            output_values[index] = output_value.to_json()
    return output_values
