
import pandas as pd
from models.grafo import Grafo
from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil


grafo1 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 4')
grafo5 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 5')


converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()

graph1 = Grafo(ponderado=True)
graph2 = Grafo(ponderado=True)
graph3 = Grafo(ponderado=True)
graph4 = Grafo(ponderado=True)
graph5 = Grafo(ponderado=True)


graph5.montar_grafo(converterUtil.convert_matrix_to_dict(grafo5))

print(graph5.adj)
print(validadorUtil.exibir_ciclo_euleriano(graph5))
