import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from models.grafo import Graph
from utils.ConverterUtil import ConverterUtil
from utils.PathUtil import PathUtil


grafo6 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 6')

converterUtil = ConverterUtil()
pathUtil = PathUtil()

graph6 = Graph(ponderado=True)

graph6.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo6))

Arvore = pathUtil.CreateSpanningTreeBFS(graph6, "D")

SpanningTree = nx.Graph()
SpanningTree.add_nodes_from(Arvore.V)

Edges = [edge for edge, cost in Arvore.edges]

SpanningTree.add_edges_from(Edges)
nx.draw(SpanningTree, with_labels=True)
plt.show()
