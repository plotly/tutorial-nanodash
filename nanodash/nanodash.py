import flask
from .components import Component
import plotly.graph_objects as go

class NanoDash:
    def __init__(self, debug=False):
        self._app = flask.Flask(__name__)
        self._debug = debug
        self._callbacks = []

        @self._app.route("/")
        def html():
            return self.full_html()

        # This route is used to handle callbacks, convert application/json content-type to dict
        @self._app.route("/state", methods=["POST"])
        def handle_change():
            response = {}
            state = flask.request.json['state']
            triggered = flask.request.json['triggered']

            response = {}
            for callback in self._callbacks:
                input_ids = callback["inputs"]
                if triggered in input_ids:
                    outputs = callback["function"]([state[triggered]])
                    outputs = self._process_outputs(outputs)
                    output_ids = callback["outputs"]
                    response.update({
                        output_id: output
                        for output_id, output in zip(output_ids, outputs)
                    })

            return response

    def set_layout(self, layout: Component):
        self.layout = layout

    def _process_outputs(self, outputs):
        for index, output in enumerate(outputs):
            if isinstance(output, go.Figure):
                outputs[index] = output.to_plotly_json()
        return outputs

    def full_html(self):
        return f"""
        <html>
            <head>
                <script src="https://cdn.plot.ly/plotly-2.32.0.min.js" charset="utf-8"></script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
                <script src='static/index.js'></script>
                <title>Simple NanoDash App</title>
            </head>
            <body>
            {self.layout.html()}
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
