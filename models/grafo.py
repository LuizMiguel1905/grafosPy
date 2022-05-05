
from collections import defaultdict

from numpy import Infinity


class Graph(object):

    def __init__(self, direcionado=False, ponderado=False):
        self.V = []  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.edges = []
        self.direcionado = direcionado
        self.ponderado = ponderado

    def addVertices(self, list):
        for v in list:
            self.graph[v] = []
        self.V = list

    def addEdgeByAdjMatrix(self, matrix):
        self.addVertices(list(matrix.keys()))
        for v in self.V:
            for n in range(len(matrix[v])):
                if matrix[v][n] > 0:
                    if not self.hasEdge(v, self.V[n]):
                        self.addEdge(v, self.V[n], peso=matrix[v][n]) if self.ponderado else self.addEdge(
                            v, self.V[n])

    def addEdge(self, u, v, peso=0):
        for edge, cost in self.edges:
            if edge == (u, v) or edge == (v, u):
                return
        self.graph[u].append(v)
        if not self.ponderado:
            self.graph[v].append(u)
        self.edges.append([(u, v), peso])

    def hasEdge(self, u, v):
        return u in self.graph and v in self.graph[u]

    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
                break
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
                break

    def getDensity(self):
        quant_arestas = len(self.edges)
        quant_vertices = len(self.V)
        equation = (2*quant_arestas)/(quant_vertices*(quant_vertices - 1))
        return 'Denso' if round(equation) == 1 else 'Esparso'

    def getVerticeDegree(self, v):
        return len(self.graph[v])

    def getVerticesGreatestDegree(self):
        vertice = list([])
        grau = 0
        for v in self.V:
            if (not(len(self.graph[v]) < grau)):
                if(len(self.graph[v]) > grau):
                    vertice = []
                grau = len(self.graph[v])
                vertice.append(v)
        return vertice

    def getVerticesLowestDegree(self):
        vertice = list([])
        grau = Infinity
        for v in self.V:
            if (not(len(self.graph[v]) > grau)):
                if(len(self.graph[v]) < grau):
                    vertice = []
                grau = len(self.graph[v])
                vertice.append(v)
        return vertice

    def getAdjVertices(self, vertice):
        return self.graph[vertice]

    def getVerticesDegreeFrequency(self):
        frequencia = dict()
        for v in self.V:
            grau = self.getVerticeDegree(v)
            if(('Grau ' + str(grau)) not in frequencia):
                frequencia['Grau ' + str(grau)] = 0
            frequencia['Grau ' + str(grau)] += 1
        return frequencia

    def __len__(self):
        return len(self.graph)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

    def __getitem__(self, v):
        return self.graph[v]
