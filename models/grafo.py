from collections import defaultdict


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
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_vertices(self, vertices):
        """ Adiciona vértices ao grafo. """
        for v in vertices:
            self.adj[v] = []



    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]