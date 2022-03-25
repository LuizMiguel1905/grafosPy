
import pandas as pd
from models.grafo import Grafo
from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil


grafo1 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 4')

converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()

graph1 = Grafo()
graph2 = Grafo()
graph3 = Grafo()
graph4 = Grafo()

adj_matrix_dict = converterUtil.convert_matrix_to_dict(grafo1)


graph1.montar_grafo(converterUtil.convert_matrix_to_dict(grafo1))
graph2.montar_grafo(converterUtil.convert_matrix_to_dict(grafo2))
graph3.montar_grafo(converterUtil.convert_matrix_to_dict(grafo3))
graph4.montar_grafo(converterUtil.convert_matrix_to_dict(grafo4))

print(validadorUtil.exibir_ciclo_euleriano(graph1))
print(validadorUtil.exibir_ciclo_euleriano(graph2))
print(validadorUtil.exibir_ciclo_euleriano(graph3))
print(validadorUtil.exibir_ciclo_euleriano(graph4))
