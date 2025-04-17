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

            # Get the state and trigger_id from the request
            state = flask.request.json["state"]
            trigger_id = flask.request.json["trigger_id"]
            print('STATE', state)

            for callback in self.callbacks:
                ## EXERCISE 5 START
                # For each callback, check if the trigger_id is in the input_ids
                # If it is, we execute the callback function to get the new values
                # for the outputs
                print('trigger_id', trigger_id)
                print('callback', callback)
                if trigger_id in callback["input_ids"]:
                    callback_function = callback["function"]
                    input_values = [
                        state[input_id] for input_id in callback["input_ids"]
                    ]
                    output_values = callback_function(input_values)

                    # If any of the outputs is not a number or a string,
                    # we convert it to a JSON-serializable dictionary
                    output_values = make_json_serializable(output_values)

                    # Update the response with the new values for the outputs
                    for output_id, output_value in zip(
                        callback["output_ids"], output_values
                    ):
                        response[output_id] = output_value
                ## EXERCISE 5 END

            # Send the response back to the frontend
            return response

    def set_layout(self, layout: Component) -> None:
        self.layout = layout

    def full_html(self) -> str:
        ## EXERCISE 1 START
        return f"""
        <html>
            <head>
                <script src="https://cdn.plot.ly/plotly-3.0.1.min.js" charset="utf-8"></script>
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
        self.callbacks.append(
            {"input_ids": input_ids, "output_ids": output_ids, "function": function}
        )

    def run(self) -> None:
        self.app.run()


def make_json_serializable(output_values: List) -> List:
    for index, output_value in enumerate(output_values):
        if isinstance(output_value, go.Figure):
            output_values[index] = output_value.to_json()
    return output_values
