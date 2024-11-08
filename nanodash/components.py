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
    
class Graph(Component):
    def __init__(self, graph_obj, attributes=None):
        super().__init__('div', [], attributes)
        self._graph_obj = graph_obj
        
    def html(self):
        attributes_html = ' '.join([f'{key}="{value}"' for key, value in self._attributes.items()])
        return f'''
                <div height="600px" width="1000px" {attributes_html}></div>
                <script>
                    var data = {self._graph_obj['data']};
                    var layout = {self._graph_obj['layout']};
                    var config = {self._graph_obj['config']};
                    Plotly.newPlot('graph', data, layout, config);
                </script>
        '''