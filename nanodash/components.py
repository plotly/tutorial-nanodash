import plotly.graph_objects as go


class Component:
    def __init__(self, **kwargs) -> None:
        raise NotImplementedError(
            f"The __init__() method for {self.__class__.__name__} is not implemented yet!"
        )

    def html(self):
        raise NotImplementedError(
            f"The html() method for {self.__class__.__name__} is not implemented yet!"
        )


class Header(Component):
    def __init__(self, id: str = "", text: str = "") -> None:
        self.id = id
        self.text = text

    def html(self) -> str:
        return f"<h1 id='{self.id}'>{self.text}</h1>"


class TextField(Component):
    def __init__(self, id: str = "") -> None:
        self.id = id

    def html(self) -> str:
        return f"<input id='{self.id}' type='text' value=''/>"


class Button(Component):
    def __init__(self, id: str = "", text: str = "") -> None:
        self.id = id
        self.text = text

    def html(self) -> str:
        return f"<button id='{self.id}'>{self.text}</button>"


class Slider(Component):
    def __init__(
        self, id: str = "", min: int = 0, max: int = 100, step: int = 1
    ) -> None:
        self.id = id
        self.min = min
        self.max = max
        self.step = step

    def html(self) -> str:
        return f"<input id='{self.id}' type='range' min='{self.min}' max='{self.max}' step='{self.step}'/>"


class Page(Component):
    def __init__(self, id: str = "", children: list = None) -> None:
        self.id = id
        self.children = children or []

    def html(self) -> str:
        return f"<div id='{self.id}'>{''.join(c.html() for c in self.children)}</div>"


class Graph(Component):
    def __init__(
        self, id: str = "", fig: dict = None, width: int = 1000, height: int = 600
    ) -> None:
        self.id = id or "graph"
        self.fig = fig or go.Figure()
        self.width = width
        self.height = height

    def html(self):
        return f"""
                <div id={self.id} height="{self.height}px" width="{self.width}px"></div>
                <script>
                    var data = {self.fig["data"]};
                    var layout = {self.fig["layout"]};
                    var config = {self.fig["config"]};
                    Plotly.newPlot('{self.id}', data, layout, config);
                </script>
        """
