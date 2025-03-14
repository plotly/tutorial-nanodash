class Component:
    def __init__(self, tag, children=None, attributes=None):
        self._tag = tag
        self._attributes = attributes or {}
        children = children or []
        self._children = children if isinstance(children, list) else [children]

    def html(self):
        attributes_html = " ".join(
            [f'{key}="{value}"' for key, value in self._attributes.items()]
        )
        children_html = [
            child.html() if isinstance(child, Component) else child
            for child in self._children
        ]
        return f"""
            <{self._tag} {attributes_html}>{"".join(children_html)}</{self._tag}>
        """


class Header(Component):
    def __init__(self, children=None, **attributes):
        super().__init__("h1", children, attributes=attributes)


class TextField(Component):
    def __init__(self, **attributes):
        super().__init__("input", attributes=attributes)


class Button(Component):
    def __init__(self, children=None, **attributes):
        super().__init__("button", children, attributes=attributes)


class Slider(Component):
    def __init__(self, **attributes):
        attributes["type"] = "range"
        super().__init__("input", attributes=attributes)


class Page(Component):
    def __init__(self, children=None, **attributes):
        super().__init__("div", children, attributes=attributes)


class Graph(Component):
    def __init__(self, fig, **attributes):
        super().__init__("div", [], attributes)
        self._fig = fig

    def html(self):
        attributes_html = " ".join(
            [f'{key}="{value}"' for key, value in self._attributes.items()]
        )
        return f"""
                <div height="600px" width="1000px" {attributes_html}></div>
                <script>
                    var data = {self._fig["data"]};
                    var layout = {self._fig["layout"]};
                    var config = {self._fig["config"]};
                    Plotly.newPlot('{self._attributes["id"]}', data, layout, config);
                </script>
        """
