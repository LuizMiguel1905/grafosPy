
import pandas as pd
from FleuryFunfanfo import Graph
from models.grafo import Grafo
from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil


grafo1 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 4')
grafo5 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 5')
grafo6 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 6')

converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()

graph1 = Graph(ponderado=True)
graph2 = Graph(ponderado=True)
graph3 = Graph(ponderado=True)
graph4 = Graph(ponderado=True)
graph5 = Graph(ponderado=True)
graph6 = Graph(ponderado=True)

graph1.add_arestas_by_adj_matrix(converterUtil.convert_matrix_to_dict(grafo1))
graph2.add_arestas_by_adj_matrix(converterUtil.convert_matrix_to_dict(grafo2))
graph3.add_arestas_by_adj_matrix(converterUtil.convert_matrix_to_dict(grafo3))
graph4.add_arestas_by_adj_matrix(converterUtil.convert_matrix_to_dict(grafo4))
graph5.add_arestas_by_adj_matrix(converterUtil.convert_matrix_to_dict(grafo5))
graph6.add_arestas_by_adj_matrix(converterUtil.convert_matrix_to_dict(grafo6))


# if ValidadorUtil.is_euleriano(graph1) != 0:
#     graph1.printEulerTour()
# if ValidadorUtil.is_euleriano(graph2) != 0:
#     graph2.printEulerTour()
# if ValidadorUtil.is_euleriano(graph3) != 0:
#     graph3.printEulerTour()
# if ValidadorUtil.is_euleriano(graph4) != 0:
#     graph4.printEulerTour()
if ValidadorUtil.is_euleriano(graph5) != 0:
    graph5.printEulerTour()
if ValidadorUtil.is_euleriano(graph6) != 0:
    graph6.printEulerTour()
