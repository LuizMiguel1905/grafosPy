import pandas as pd
from models.grafo import Graph

from utils.BellmanFord import BelmanFord
from utils.ConverterUtil import ConverterUtil

grafo1 = pd.read_excel("docs/grafos/Bellman_Ford.xlsx", sheet_name='Grafo1')
grafo2 = pd.read_excel("docs/grafos/Bellman_Ford.xlsx", sheet_name='Grafo2')

converterUtil = ConverterUtil()
bf = BelmanFord()

graph1 = Graph(ponderado=True,  direcionado=True)
graph2 = Graph(ponderado=True,  direcionado=True)
graph3 = Graph(ponderado=True,  direcionado=True)

graph1.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo1))
graph2.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo2))

graph3.addVertices(['h', 'i', 'j'])
graph3.addEdge('h', 'i', 2)
graph3.addEdge('i', 'j', 3)
graph3.addEdge('j', 'h', -8)
bf.solve(graph1, "S")