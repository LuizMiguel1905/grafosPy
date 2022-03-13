import pandas as pd
from models.grafo import Grafo
from models.MatrixConverter import MatrixConverter

grafo1 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 4')


MC = MatrixConverter(grafo1)

vertices = MC.convert_collumn_to_list('V')
adj_matrix_dict = MC.convert_matrix_to_dict('V')
graph = Grafo(vertices)
graph.add_arestas_by_adj_matrix(adj_matrix_dict)

print(graph.existe_aresta('A', 'E'))
