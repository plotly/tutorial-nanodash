import flask
from .components import Component

class NanoDash:
    def __init__(self, debug=False):
        self._app = flask.Flask(__name__)
        self._debug = debug

    def set_layout(self, layout: Component):
        # Create a simple route
        # TODO: figure out how to write this so that
        # you can call set_layout multiple times without
        # crashing the app. 
        @self._app.route('/')
        def home():
            return layout.html()

    def run(self):
        # Run the web server in debug mode
        self._app.run( debug=self._debug )