import pandas as pd

from models.grafo import Graph
from utils.PathUtil import PathUtil

from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil
from utils.PathUtil import PathUtil

grafo1 = pd.read_excel("docs/grafos/atividade04.xlsx")

converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()
pathUtil = PathUtil()

graph1 = Graph(ponderado=False)

graph1.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo1))

novoGrafo = PathUtil()

novoGrafo.BFS(graph1, 1)