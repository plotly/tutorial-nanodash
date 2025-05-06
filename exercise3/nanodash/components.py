"""
This file contains class definitions for individual components
that can be used to build a dashboard in NanoDash.
"""

import plotly.graph_objects as go


class Component:
    def __init__(self, **kwargs) -> None:
        """
        Initiaize the component.
        """
        raise NotImplementedError(
            f"The __init__() method for {self.__class__.__name__} is not implemented yet!"
        )

    def html(self) -> str:
        """
        Returns a string containing the HTML needed to render this component
        in the page layout.
        """
        raise NotImplementedError(
            f"The html() method for {self.__class__.__name__} is not implemented yet!"
        )


class Page(Component):
    def __init__(self, id: str = "", children: list = None) -> None:
        self.id = id
        self.children = children or []

    def html(self) -> str:
        return f"<div id='{self.id}'>{''.join(c.html() for c in self.children)}</div>"


class Header(Component):
    def __init__(self, id: str = "", text: str = "") -> None:
        self.id = id
        self.text = text

    def html(self) -> str:
        return f"<h1 id='{self.id}'>{self.text}</h1>"


class Text(Component):
    def __init__(self, id: str = "", text: str = "") -> None:
        self.id = id
        self.text = text

    def html(self) -> str:
        return f"<p id='{self.id}'>{self.text}</p>"


class TextInput(Component):
    def __init__(self, id: str = "", value="") -> None:
        self.id = id
        self.value = value

    def html(self) -> str:
        ## EXERCISE 2 START
        return f"<input id='{self.id}' type='text' value='{self.value}'/>"
        ## EXERCISE 2 END


class Dropdown(Component):
    def __init__(self, id: str = "", options: list = None, value=None) -> None:
        self.id = id
        self.options = options or []
        self.value = value

    def html(self) -> str:
        ## EXERCISE 2 START
        options_html = [
            f"<option value='{opt}'{' selected' if opt == self.value else ''}>{opt}</option>"
            for opt in self.options
        ]
        options_html_joined = "".join(options_html)
        return f"<select id='{self.id}'>{options_html_joined}</select>"
        ## EXERCISE 2 END


class Button(Component):
    def __init__(self, id: str = "", text: str = "") -> None:
        self.id = id
        self.text = text

    def html(self) -> str:
        return f"<button id='{self.id}'>{self.text}</button>"


class Slider(Component):
    def __init__(
        self, id: str = "", min: int = 0, max: int = 100, step: int = 1, value=None
    ) -> None:
        self.id = id
        self.min = min
        self.max = max
        self.step = step
        self.value = value

    def html(self) -> str:
        return f"<input id='{self.id}' value='{self.value}' type='range' min='{self.min}' max='{self.max}' step='{self.step}'/>"


class Graph(Component):
    def __init__(
        self, id: str = "", fig: go.Figure = None, width: int = 1000, height: int = 600
    ) -> None:
        self.id = id or "graph"
        self.fig = fig or go.Figure()
        self.width = width
        self.height = height

    def html(self):
        # For an example of how to embed a Plotly graph in HTML, see:
        # https://codepen.io/marthacryan/pen/yyyyOoB
        #
        # You will also need to use the JSON string representation of the Plotly figure object.
        # This can be obtained using the to_json() method of the Figure class:
        #
        #     fig_as_json_string = fig.to_json()

        ## EXERCISE 3 START
        raise NotImplementedError(
            "The html() method of the Graph class is not implemented yet!"
        )
        ## EXERCISE 3 END
