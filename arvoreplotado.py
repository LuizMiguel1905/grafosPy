import pydot

graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white')


graph.add_node(pydot.Node('1', shape='circle'))
graph.add_node(pydot.Node('2', shape='circle'))
graph.add_node(pydot.Node('3', shape='circle'))
graph.add_node(pydot.Node('4', shape='circle'))
graph.add_node(pydot.Node('5', shape='circle'))

graph.add_edge(pydot.Edge('1', '2', color='blue'))
graph.add_edge(pydot.Edge('2', '5', color='blue'))
graph.add_edge(pydot.Edge('5', '3', color='blue'))
graph.add_edge(pydot.Edge('4', '5', color='blue'))
graph.add_edge(pydot.Edge('1', '5', color='blue'))

output_graphviz_svg = graph.create_svg()
graph.write_png('naooutput.png')
