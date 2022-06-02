import pandas as pd
from models.grafo import Graph


from utils.ConverterUtil import ConverterUtil
from utils.FloydWarshall import FloydWarshall

grafo1 = pd.read_excel("docs/grafos/Floyd_Warshall.xlsx", sheet_name='Grafo1')
grafo2 = pd.read_excel("docs/grafos/Floyd_Warshall.xlsx", sheet_name='Grafo2')

converterUtil = ConverterUtil()
fw = FloydWarshall()

graph1 = Graph(ponderado=True,  direcionado=True)
graph2 = Graph(ponderado=True)
graph3 = Graph(ponderado=True,  direcionado=True)

graph3.addVertices(['A', 'B', 'C'])
graph3.addEdge('A', 'B', 4)
graph3.addEdge('A', 'C', 11)
graph3.addEdge('B', 'A', 6)
graph3.addEdge('B', 'C', 2)
graph3.addEdge('C', 'A', 3)

graph1.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo1))
graph2.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo2))


# fw.solve(graph3)
print("------------------------------------------")
fw.solve(graph2)
print("------------------------------------------")
