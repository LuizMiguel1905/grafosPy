import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import networkx as nx

from models.grafo import Grafo
from models.MatrixConverter import MatrixConverter
from itertools import islice

file = pd.read_excel("docs/matriz_adj_uf_brasil.xlsx",)

MC = MatrixConverter(file)


graph = Grafo(MC.convert_collumn_to_list('UF'))

graph.add_arestas_by_adj_matrix(MC.convert_matrix_to_dict('UF'))


##Apresentação dos dados 
print('--------------------------------------------------------------------')
print('Vértice de maior grau: ' + str(graph.get_vertices_maior_grau()))
print('Grau: ' + str(len(graph.adj[graph.get_vertices_maior_grau()[0]])))
print('Vizinhos: ' + str(graph.get_vizinhos(graph.get_vertices_maior_grau())))
print('--------------------------------------------------------------------')
print('Vértice de menor grau: ' + str(graph.get_vertices_menor_grau()))
print('Grau: ' + str(len(graph.adj[graph.get_vertices_menor_grau()[0]])))
print('Vizinhos: ' + str(graph.get_vizinhos(graph.get_vertices_menor_grau())))
print('--------------------------------------------------------------------')
print('Densidade do grafo: ' + str(graph.get_densidade()))
print('--------------------------------------------------------------------')
print('Frequencia de graus dos vértices: ')
graphList = graph.get_freq_grau_vertices().items()
print(sorted(graphList))

#Histograma

data = []
#=-=-=-=-=-=-=-=-=Adicionando a frequencia de graus dos vértices em uma tupla -=-=-=-=-=-=-=#

for itens in graph.get_freq_grau_vertices().items():
    for i in range(itens[1]):
        data.append(itens[0])
plt2.hist(sorted(data), 7, rwidth=0.9)
plt2.show()

#-==-=-=-=-=-=-==-GRAFO-=-==--==---=-===-=
G = nx.Graph()
#Loop para criar as vertices do grafo
for x in graph.get_vertices():
    G.add_node(x)

#Loop para criar as arestas do grafo
for k in graph.adj.keys():
    for v in graph.adj[k]:
        if((str(k), str(v)) and (str(v), str(k))):
             G.add_edge(k, v)

nx.draw(G, with_labels = True)

#Exibir o grafo
plt.show()

