from asyncio.windows_events import NULL
from collections import defaultdict

from numpy import Infinity


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, direcionado=False, ponderado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict()
        self.vertices = []
        self.arestas = []
        self.direcionado = direcionado
        self.ponderado = ponderado

    def montar_grafo(self, matrix):
        self.adiciona_vertices(matrix.keys())
        self.add_arestas_by_adj_matrix(matrix)

    def add_arestas_by_adj_matrix(self, matrix):
        """ Adiciona as conexãões aos vértices através da """
        for v in self.get_vertices():
            self.adj[v] = self.get_vertices_adjacentes_por_linha(matrix[v])

    def get_vertices(self):
        return self.vertices

    def get_vertices_adjacentes_por_linha(self, line):
        """ Retorna uma lista dos vértices representados em uma linha da matriz"""
        connect_list = list()
        for n in range(len(line)):
            if line[n] > 0:
                if self.ponderado:
                    connect_list.append([self.get_vertices()[n], line[n]])
                else:
                    connect_list.append([self.get_vertices()[n], 0])
        return connect_list

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        if self.arestas == []:
            resp = list()
            for k in self.adj.keys():
                for v in self.adj[k]:
                    if((str(k) + str(v[0])) and (str(v[0]) + str(k)) not in resp):
                        resp.append((str(k) + str(v[0])))
            self.arestas = resp
        return self.arestas

    def adiciona_vertices(self, vertices):
        """ Adiciona vértices ao grafo. """
        for v in vertices:
            self.adj[v] = []
        self.vertices = list(self.adj.keys())

    def get_densidade(self):
        quant_arestas = len(self.get_arestas())
        quant_vertices = len(self.get_vertices())
        eq = (2*quant_arestas)/(quant_vertices*(quant_vertices - 1))
        resp = ''
        if round(eq) == 1:
            resp = 'Denso'
        else:
            resp = 'Esparso'
        return(resp)

    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        if u in self.adj:
            for itens in self.adj[u]:
                if itens[0] == v:
                    return True
        return False

    def get_grau_vertice(self, v):
        return len(self.adj[v])

    def get_vertices_maior_grau(self):
        vertice = list([])
        grau = 0
        for v in self.get_vertices():
            if (not(len(self.adj[v]) < grau)):
                if(len(self.adj[v]) > grau):
                    vertice = []
                grau = len(self.adj[v])
                vertice.append(v)
        return vertice

    def get_vertices_menor_grau(self):
        vertice = list([])
        grau = Infinity
        for v in self.get_vertices():
            if (not(len(self.adj[v]) > grau)):
                if(len(self.adj[v]) < grau):
                    vertice = []
                grau = len(self.adj[v])
                vertice.append(v)
        return vertice

    def get_vertices_adjacentes(self, vertice):
        resposta = []
        for v in self.adj[vertice]:
            resposta.append(v[0])
        return resposta

    def get_freq_grau_vertices(self):
        frequencia = dict()
        for v in self.get_vertices():
            grau = len(self.adj[v])
            if(('Grau ' + str(grau)) not in frequencia):
                frequencia['Grau ' + str(grau)] = 0
            frequencia['Grau ' + str(grau)] += 1
        return frequencia

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]
