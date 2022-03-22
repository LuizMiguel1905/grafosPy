from tkinter import X
from re import A
import pandas as pd
from models.grafo import Grafo
from models.MatrixConverter import MatrixConverter


grafo1 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("docs/Grafos/Grafos.xlsx", sheet_name='Grafo 4')


MC = MatrixConverter(grafo1)

vertices = MC.convert_collumn_to_list('V')
adj_matrix_dict = MC.convert_matrix_to_dict('V')
graph = Grafo(vertices)
graph.add_arestas_by_adj_matrix(adj_matrix_dict)

def eurelianoVerify():
    newList = []
    imparCount = 0
    for x in graph.get_vertices():
        if graph.get_grau_vertice(x) % 2 == 0:
            newList.append(1)
        else:
            newList.append(0)
            imparCount = imparCount + 1

    print(newList)            
    if 0 in newList and imparCount == 2:
        print("Semi-Eureliano")
    if 0 in newList and imparCount > 2:
        print("Não eureliano")
    if 1 in newList and imparCount == 0:
        print("Eureliano")

eurelianoVerify()