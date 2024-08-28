class Component:
    def __init__(self, tag, children, attributes=None):
        self._tag = tag
        self._attributes = attributes or {}
        self._children = children if isinstance(children, list) else [children]
        
    def html(self):
        attributes_html = ' '.join([f'{key}="{value}"' for key, value in self._attributes.items()])
        children_html = [child.html() if isinstance(child, Component) else child for child in self._children]
        return f'''
                <{self._tag} {attributes_html}>{"".join(children_html)}</{self._tag}>
        '''