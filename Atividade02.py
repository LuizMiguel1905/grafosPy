from tkinter import X
from re import A
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

print("Grafo 1: ")
print("Ore: ")
ValidadorUtil.is_hamiltoniano_Ore(graph1)
print("Dirac: ")
ValidadorUtil.is_hamiltoniano_Dirac(graph1)
print("Bondy Chvatal: ")
ValidadorUtil.is_hamiltoniano_Bondy_Chvatal(graph1)
print('----------------------------------------------------------')
print("Grafo 2: ")
print("Ore: ")
ValidadorUtil.is_hamiltoniano_Ore(graph2)
print("Dirac: ")
ValidadorUtil.is_hamiltoniano_Dirac(graph2)
print("Bondy Chvatal: ")
ValidadorUtil.is_hamiltoniano_Bondy_Chvatal(graph2)
print('----------------------------------------------------------')
print("Grafo 3: ")
print("Ore: ")
ValidadorUtil.is_hamiltoniano_Ore(graph3)
print("Dirac: ")
ValidadorUtil.is_hamiltoniano_Dirac(graph3)
print("Bondy Chvatal: ")
ValidadorUtil.is_hamiltoniano_Bondy_Chvatal(graph3)
print('----------------------------------------------------------')
print("Grafo 4: ")
print("Ore: ")
ValidadorUtil.is_hamiltoniano_Ore(graph4)
print("Dirac: ")
ValidadorUtil.is_hamiltoniano_Dirac(graph4)
print("Bondy Chvatal: ")
ValidadorUtil.is_hamiltoniano_Bondy_Chvatal(graph4)
