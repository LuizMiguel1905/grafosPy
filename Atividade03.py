
import pandas as pd
from models.grafo import Graph
from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil
from utils.PathUtil import PathUtil

grafo1 = pd.read_excel("grafosPy/docs/Grafos/Grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("grafosPy/docs/Grafos/Grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("grafosPy/docs/Grafos/Grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("grafosPy/docs/Grafos/Grafos.xlsx", sheet_name='Grafo 4')
grafo5 = pd.read_excel("grafosPy/docs/Grafos/Grafos.xlsx", sheet_name='Grafo 5')


converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()
pathUtil = PathUtil()

graph1 = Graph(ponderado=True)
graph2 = Graph(ponderado=True)
graph3 = Graph(ponderado=True)
graph4 = Graph(ponderado=True)
graph5 = Graph(ponderado=True)


graph1.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo1))
graph2.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo2))
graph3.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo3))
graph4.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo4))
graph5.addEdgeByAdjMatrix(converterUtil.convertMatrixToDict(grafo5))


pathUtil.printEulerTour(graph1) if ValidadorUtil.isEulerian(
    graph1) != 0 else print("Grafo 1 não é euleriano")

pathUtil.printEulerTour(graph2) if ValidadorUtil.isEulerian(
    graph2) != 0 else print("Grafo 2 não é euleriano")

pathUtil.printEulerTour(graph3) if ValidadorUtil.isEulerian(
    graph3) != 0 else print("Grafo 3 não é euleriano")

pathUtil.printEulerTour(graph4) if ValidadorUtil.isEulerian(
    graph4) != 0 else print("Grafo 4 não é euleriano")

pathUtil.printEulerTour(graph5) if ValidadorUtil.isEulerian(
    graph5) != 0 else print("Grafo 5 não é euleriano")
