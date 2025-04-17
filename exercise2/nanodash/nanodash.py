import flask

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
                <script src='static/index.js'></script>
                <title>{self.title}</title>
            </head>
            <body>
            {self.layout.html()}
            </body>
        </html>
        """
        ## EXERCISE 1 END

    def run(self) -> None:
        """
        Run the NanoDash application by starting the Flask server.
        """
        self.app.run()
