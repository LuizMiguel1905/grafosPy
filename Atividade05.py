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

Arvore1 = pathUtil.CreateSpanningTreeDFSRecursive(graph7, "B")
Arvore2 = pathUtil.CreateSpanningTreeDFSStack(graph7, "B")

SpanningTree = nx.Graph()
SpanningTree2 = nx.Graph()
SpanningTree.add_nodes_from(Arvore1.V)
SpanningTree2.add_nodes_from(Arvore2.V)

Edges = [edge for edge, cost in Arvore1.edges]

Edges2 = [edge for edge, cost in Arvore2.edges]
SpanningTree.add_edges_from(Edges)
SpanningTree2.add_edges_from(Edges2)

nx.draw(SpanningTree, with_labels=True)
plt.title("Spanning Tree Recursiva")
plt.show()
nx.draw(SpanningTree2, with_labels=True)
plt.title("Spanning Tree com Pilha")
plt.show()
