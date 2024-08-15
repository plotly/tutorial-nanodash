class Component:
    def __init__(self, tag, children):
        self._tag = tag
        self._children = children if isinstance(children, list) else [children]
        
    def html(self):
        children_html = [child.html() if isinstance(child, Component) else child for child in self._children]
        return f'<{self._tag}>{"".join(children_html)}</{self._tag}>'