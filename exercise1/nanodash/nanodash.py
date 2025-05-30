"""
This file contains the definition for the NanoDash class itself,
including logic for running the Flask server, returning the HTML layout
of the app, and handling callbacks.
"""

import flask


class NanoDash:
    def __init__(self, title: str = "NanoDash App") -> None:
        self.app = flask.Flask(__name__)
        self.title = title

        # This route is used to serve the main HTML page
        @self.app.route("/")
        def html() -> str:
            """
            Receives a request from the browser and returns the HTML
            for the main page.
            """
            return self.full_html()

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
        raise NotImplementedError(
            "The full_html() method of the NanoDash class is not implemented yet!"
        )
        ## EXERCISE 1 END

    def run(self, debug=True, **kwargs) -> None:
        """
        Run the NanoDash application by starting the Flask server.
        """
        self.app.run(debug=debug, **kwargs)
