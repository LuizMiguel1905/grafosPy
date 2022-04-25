import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from models.grafo import Graph
from utils.ConverterUtil import ConverterUtil
from utils.PathUtil import PathUtil


grafo7 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 7')

converterUtil = ConverterUtil()
pathUtil = PathUtil()

graph7 = Graph(ponderado=True)

graph7.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo7))

Arvore = pathUtil.CreateSpanningTreeDFSStack(graph7, "D")

SpanningTree = nx.Graph()
SpanningTree.add_nodes_from(graph7.V)

Edges = [edge for edge, cost in Arvore.edges]

SpanningTree.add_edges_from(Edges)
nx.draw(SpanningTree, with_labels=True)
plt.show()
