from nanodash.components import Component

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