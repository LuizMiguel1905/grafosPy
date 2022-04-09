
from asyncio.windows_events import NULL
from numpy import Infinity
import pandas as pd


class ConverterUtil(object):

    def convert_matrix_collumn_to_list(self, file, collumn):
        df = pd.DataFrame(file, columns=[collumn]).values
        newList = list()
        for value in df:
            newList.append(value[0])
        return newList

    def convert_matrix_to_dict(self, file):
        adjacency_list = dict()
        keys = (list(file.iloc[:, 0]))
        for key in keys:
            connection = self.convert_matrix_collumn_to_list(file, key)

            adjacency_list[key] = connection
        return adjacency_list

    def BFS(grafo, rootnode):
        color = ('white') * len(grafo.V)
        distance = (Infinity) * len(grafo.V)
        parent = (None) * len(grafo.V)

        RootIndex = grafo.V.index(rootnode)
        color[RootIndex] = 'gray'
        distance[RootIndex] = 0
        Q = []
        Q.append(rootnode)
        while not Q:
            u = Q.pop()
            for v in grafo.graph[u]:
                if color[grafo.V.index(v)] == 'white':
                    color[grafo.V.index(v)] = 'gray'
                    distance[grafo.V.index(v)] = distance[grafo.V.index(u)] + 1
                    parent[grafo.V.index(v)] = 'u'
            color[grafo.V.index(u)] = 'black'
