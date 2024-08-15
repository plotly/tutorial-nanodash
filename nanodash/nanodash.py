import flask

class NanoDash:
    def __init__(self):
        self._app = flask.Flask(__name__)

    def set_layout(self, layout):
        # Create a simple route
        # TODO: figure out how to write this so that
        # you can call set_layout multiple times without
        # crashing the app. 
        @self._app.route('/')
        def home():
            return layout

    def run(self):
        # Run the web server in debug mode
        self._app.run( debug=True )