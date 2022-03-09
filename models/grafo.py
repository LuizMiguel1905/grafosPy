from asyncio.windows_events import NULL
from collections import defaultdict

from numpy import Infinity


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, vertices, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict()
        self.direcionado = direcionado
        self.adiciona_vertices(vertices)

    def add_arestas_by_adj_matrix(self, matrix):
        """ Adiciona as conexãões aos vértices através da """
        for v in self.get_vertices():
            self.adj[v] = self.has_connections_by_line(matrix[v])

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())

    def has_connections_by_line(self, line):
        """ Retorna uma lista dos vértices representados em uma linha da matriz"""
        connect_list = list()
        for n in range(len(line)):
            if line[n] == 1:
                connect_list.append(self.get_vertices()[n])
        return connect_list

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        resp = list()
        for k in self.adj.keys():
            for v in self.adj[k]:
                if((str(k), str(v)) and (str(v), str(k)) not in resp):
                    resp.append((str(k), str(v)))
        return resp
 

    def adiciona_vertices(self, vertices):
        """ Adiciona vértices ao grafo. """
        for v in vertices:
            self.adj[v] = []

    def get_densidade(self):
        quant_arestas = len(self.get_arestas())  
        quant_vertices = len(self.get_vertices()) 
        eq =(2*quant_arestas)/(quant_vertices*(quant_vertices - 1))
        resp = ''
        if round(eq) == 1:
            resp = 'Denso'
        else:
            resp = 'Esparso'
        return(resp)        


    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]

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

    def get_vizinhos(self,vertice):
        if (type(vertice) is list):
            resposta = dict()
            for v in vertice:
                resposta[v] = self.adj[v]
            return resposta
        else:
            resposta = self.adj[v]       
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