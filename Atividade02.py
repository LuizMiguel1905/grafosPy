from tkinter import X
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





def dirac():
    newList = []
    if len(graph.get_vertices()) >= 3:
        for x in graph.get_vertices():
            if graph.get_grau_vertice(x) >= len(graph.get_vertices()) / 2:
                newList.append(1)
            else:
                newList.append(0)
    print(newList)            
    if 0 in newList:
        print("False")
    else:
        print("True")


def bondy():
    newList = []
    nAdjacente = []
    for y in graph.get_vertices():
        for x in graph.get_vertices():
            if x not in graph.get_vertices_adjacentes(y):
                nAdjacente.append(x)
        nAdjacente.remove(y)
        
        soma = 0
        for x in nAdjacente:
            soma += graph.get_grau_vertice(x)
        
        if soma >= len(graph.get_vertices()):
            newList.append(1)
        else:
            newList.append(0)
    
    print(newList)
    if 0 in newList:
        print("False")
    else:
        print("True")
        
dirac()
print(graph.get_grau_vertice("C"))