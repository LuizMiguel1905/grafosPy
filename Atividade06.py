import pandas as pd

from models.grafo import Graph
from utils.PathUtil import PathUtil

from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil
from utils.PathUtil import PathUtil

from utils.Dijsktra import Dijsktra

grafo1 = pd.read_excel("docs/grafos/grafoII.xlsx", sheet_name='grafo1')
grafo2 = pd.read_excel("docs/grafos/grafoII.xlsx", sheet_name='grafo2')
#grafo3 = pd.read_excel("docs/grafos/grafoII.xlsx", sheet_name='grafo3')
converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()
pathUtil = PathUtil()

disk = Dijsktra()

#graph1 = Graph(ponderado=True,  direcionado=True)
graph2 = Graph(ponderado=True,  direcionado=True)
#graph3 = Graph(ponderado=True,  direcionado=False)
#graph1.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo1))
graph2.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo2))
#graph3.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo3))

#disk.dijkstra(graph1, "A")
disk.dijkstra(graph2, "A")



