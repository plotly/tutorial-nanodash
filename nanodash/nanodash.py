import flask
from .components import Component

class NanoDash:

    def __init__(self, debug=False):
        self._app = flask.Flask(__name__)
        self._debug = debug
        self._callbacks = []

        # This route is used to handle callbacks
        @self._app.route('/state', methods=['POST'])
        def handle_change():
            print(dict(flask.request.form))

            # TODO: Update this logic to correctly choose which callback(s) to run
            # TODO: Handle prop names (right now we are assuming everything is `value`)
            for k, v in dict(flask.request.form).items():
                for callback in self._callbacks:
                    for input in callback['inputs']:
                        if input[0] == k:
                            outputs = callback['function']([v])
                            output_names = [_k for _k, _ in callback['outputs']]
                            response = {
                                output_name: output for output_name, output in zip(output_names, outputs)
                            }
                            break

            return response

    def set_layout(self, layout: Component):
        # Create a simple route
        # TODO: figure out how to write this so that
        # you can call set_layout multiple times without
        # crashing the app. 
        @self._app.route('/')
        def home():
            return f'''
        <html>
            <head>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
                <script src='static/layoutState.js'></script>
                <title>Simple NanoDash App</title>
            </head>
            <body>
            {layout.html()}
            </body>
        </html>
        '''

    def add_callback(self, inputs, outputs, function):
        self._callbacks.append({
            'inputs': inputs,
            'outputs': outputs,
            'function': function
        })

    def run(self):
        # Run the web server in debug mode
        self._app.run(debug=self._debug)
