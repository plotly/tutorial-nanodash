import flask
from .components import Component

class NanoDash:
    _state = {}

    def __init__(self, debug=False):
        self._app = flask.Flask(__name__)
        self._debug = debug

        # This route is used to handle callbacks
        @self._app.route('/state', methods=['POST'])
        def handle_change():
            # TODO: use the given state to update the displayed layout
            print(dict(flask.request.form))
            return 'OK'

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

    def run(self):
        # Run the web server in debug mode
        self._app.run( debug=self._debug )