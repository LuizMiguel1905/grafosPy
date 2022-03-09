import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import networkx as nx

from models.grafo import Grafo
from itertools import islice

file = pd.read_excel("./matriz_adj_uf_brasil.xlsx",)

def df_to_list(state):
    df = pd.DataFrame(file,columns=[state]).values
    newList = list()
    for value in df:
        newList.append(value[0])
    return newList

print(file);

#Vértices em forma de lista
estados = pd.DataFrame(file,columns=['UF']).values
states = set()
for siglas in estados:
    states.add(siglas[0])
    
states = sorted(states)

adjacency_list = dict()

for state in states:
    connection = df_to_list(state)
    print(state  + ': ' + str(connection))
    adjacency_list[state] = connection

graph = Grafo(states)

graph.add_arestas_by_adj_matrix(adjacency_list)



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
data = ['Grau 1', 'Grau 1', 'Grau 1', 'Grau 2' , 'Grau 2' , 'Grau 2' , 'Grau 2' , 'Grau 2', 'Grau 3',  'Grau 3' , 'Grau 3'
, 'Grau 3' , 'Grau 3' , 'Grau 3' , 'Grau 3', 'Grau 4', 'Grau 4', 'Grau 5' , 'Grau 5' , 'Grau 5' , 'Grau 5' , 'Grau 6'
, 'Grau 6', 'Grau 6', 'Grau 6', 'Grau 6', 'Grau 8']

plt2.hist(data, 7, rwidth=0.9)
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

