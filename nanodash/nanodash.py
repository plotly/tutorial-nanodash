import flask
from .components import Component
import plotly.graph_objects as go

def process_outputs(outputs):
    for index, output in enumerate(outputs):
        if isinstance(output, go.Figure):
            outputs[index] = output.to_plotly_json()
    return outputs

class NanoDash:
    def __init__(self, debug=False):
        self._app = flask.Flask(__name__)
        self._debug = debug
        self._callbacks = []

        # This route is used to handle callbacks, convert application/json content-type to dict
        @self._app.route("/state", methods=["POST"], )
        def handle_change():
            response = {}
            state = flask.request.json['state']
            triggered = flask.request.json['triggered']
            # TODO: Handle prop names (right now we are assuming everything is `value`)

            response = {}
            for callback in self._callbacks:
                input_names = [input_name for input_name, _ in callback["inputs"]]
                if triggered in input_names:
                    outputs = callback["function"]([state[triggered]])
                    outputs = process_outputs(outputs)
                    output_names = [output_name for output_name, _ in callback["outputs"]]
                    response.update({
                        output_name: output
                        for output_name, output in zip(output_names, outputs)
                    })

            return response

    def set_layout(self, layout: Component):
        # Create a simple route
        # TODO: figure out how to write this so that
        # you can call set_layout multiple times without
        # crashing the app.
        @self._app.route("/")
        def home():
            return f"""
        <html>
            <head>
                <script src="https://cdn.plot.ly/plotly-2.32.0.min.js" charset="utf-8"></script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
                <script src='static/layoutState.js'></script>
                <title>Simple NanoDash App</title>
            </head>
            <body>
            {layout.html()}
            </body>
        </html>
        """

    def add_callback(self, inputs, outputs, function):
        self._callbacks.append(
            {"inputs": inputs, "outputs": outputs, "function": function}
        )

    def run(self):
        # Run the web server in debug mode
        self._app.run(debug=self._debug)
