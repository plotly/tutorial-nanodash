"""
This file contains class definitions for individual components
that can be used to build a dashboard in NanoDash.
"""


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
        raise NotImplementedError(
            "The html() method of the TextInput class is not implemented yet!"
        )
        ## EXERCISE 2 END


class Dropdown(Component):
    def __init__(self, id: str = "", options: list = None, value=None) -> None:
        self.id = id
        self.options = options or []
        self.value = value

    def html(self) -> str:
        ## EXERCISE 2 START
        raise NotImplementedError(
            "The html() method of the Dropdown class is not implemented yet!"
        )
        ## EXERCISE 2 END
