
import pandas as pd
from models.grafo import Grafo
from models.MatrixConverter import MatrixConverter
import copy

grafo1 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 1')
grafo2 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 2')
grafo3 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 3')
grafo4 = pd.read_excel("docs/grafos/grafos.xlsx", sheet_name='Grafo 4')


MC = MatrixConverter(grafo1)

vertices = MC.convert_collumn_to_list('V')
adj_matrix_dict = MC.convert_matrix_to_dict('V')
graph1 = Grafo(vertices)
graph1.add_arestas_by_adj_matrix(adj_matrix_dict)

MC.set_file(grafo2)

vertices = MC.convert_collumn_to_list('V')
adj_matrix_dict = MC.convert_matrix_to_dict('V')
graph2 = Grafo(vertices)
graph2.add_arestas_by_adj_matrix(adj_matrix_dict)

MC.set_file(grafo3)

vertices = MC.convert_collumn_to_list('V')
adj_matrix_dict = MC.convert_matrix_to_dict('V')
graph3 = Grafo(vertices)
graph3.add_arestas_by_adj_matrix(adj_matrix_dict)

MC.set_file(grafo4)

vertices = MC.convert_collumn_to_list('V')
adj_matrix_dict = MC.convert_matrix_to_dict('V')
graph4 = Grafo(vertices)
graph4.add_arestas_by_adj_matrix(adj_matrix_dict)


def dirac(grafo):
    newList = []
    if len(grafo.get_vertices()) >= 3:
        for x in grafo.get_vertices():
            if grafo.get_grau_vertice(x) < len(grafo.get_vertices()) / 2:
                return False
    return True


def Ore(grafo):
    vList = grafo.get_vertices()
    nn = len(vList)
    if (nn > 3):
        for n in vList:
            newList = []
            for x in grafo.get_vertices():
                if x not in grafo.get_vertices_adjacentes(n):
                    newList.append(x)
                    current_Vertice = n
            newList.remove(n)
            for k in newList:
                if(grafo.get_grau_vertice(current_Vertice) + grafo.get_grau_vertice(k) < nn):
                    return False
        return True


def bondy(grafo):
    nAdjacente = []
    nn = len(grafo.get_vertices())
    current_v = ""
    gCopia = copy.deepcopy(grafo)
    for y in gCopia.get_vertices():
        for x in gCopia.get_vertices():
            if x not in gCopia.get_vertices_adjacentes(y):
                nAdjacente.append(x)
                current_v = y
        nAdjacente.remove(y)

        for k in nAdjacente:
            if(grafo.get_grau_vertice(current_v) + grafo.get_grau_vertice(k) >= nn):
                gCopia.add_aresta(current_v, k)
    for v in gCopia.get_vertices():
        if gCopia.get_grau_vertice(v) != nn - 1:
            return False
    return True


print("Grafo 1:")
print("Teorema de Ore: " + str(Ore(graph1)))
print("Teorema de Dirac: " + str(dirac(graph1)))
print("Teorema de bondy: " + str(bondy(graph1)))

print("Grafo 2:")
print("Teorema de Ore: " + str(Ore(graph2)))
print("Teorema de Dirac: " + str(dirac(graph2)))
print("Teorema de bondy: " + str(bondy(graph2)))


print("Grafo 3:")
print("Teorema de Ore: " + str(Ore(graph3)))
print("Teorema de Dirac: " + str(dirac(graph3)))
print("Teorema de bondy: " + str(bondy(graph3)))


print("Grafo 4:")
print("Teorema de Ore: " + str(Ore(graph4)))
print("Teorema de Dirac: " + str(dirac(graph4)))
print("Teorema de bondy: " + str(bondy(graph4)))
