
import pandas as pd
import numpy as np

from models.grafo import Grafo

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

graph.add_arestas_by_adj_list(adjacency_list)

print(graph.adj)



