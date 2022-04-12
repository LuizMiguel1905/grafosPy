import pandas as pd
from models.grafo import Graph
from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil
from utils.PathUtil import PathUtil

grafo6 = pd.read_excel("grafosPy/docs/Grafos/Grafos.xlsx", sheet_name='Grafo 6')

converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()
pathUtil = PathUtil()

graph6 = Graph(ponderado=True)

graph6.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo6))

pathUtil.BFS(graph6, "E")