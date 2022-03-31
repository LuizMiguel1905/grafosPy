import pandas as pd

from collections import defaultdict

# This class represents an undirected graph using adjacency list representation


class Graph:

    def __init__(self, direcionado=False, ponderado=False):
        self.V = []  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
        self.arestas = []
        self.direcionado = direcionado
        self.ponderado = ponderado

    def add_arestas_by_adj_matrix(self, matrix):
        self.V = list(matrix.keys())
        for v in self.V:
            for n in range(len(matrix[v])):
                if matrix[v][n] > 0:
                    if self.ponderado:
                        if not self.hasEdge(v, self.V[n]):
                            self.addEdge(v, self.V[n], peso=matrix[v][n])
                    else:
                        if not self.hasEdge(v, self.V[n]):
                            self.addEdge(v, self.V[n])

    # function to add an edge to graph

    def addEdge(self, u, v, peso=0):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.arestas.append([str(u + v), peso])

    def hasEdge(self, u, v):
        return u in self.graph and v in self.graph[u]

    # This function removes edge u-v from graph

    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    # A DFS based function to count reachable vertices from v
    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        return count

    # The function to check if edge u-v can be considered as next edge in
    # Euler Tour
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:

        #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge

            2.a) count of vertices reachable from u'''
            visited = [False]*(len(self.V))
            count1 = self.DFSCount(self.V.index(u), visited)

            '''2.b) Remove edge (u, v) and after removing the edge, count
                vertices reachable from u'''
            self.rmvEdge(u, v)
            visited = [False]*(len(self.V))
            count2 = self.DFSCount(self.V.index(u), visited)

            # 2.c) Add the edge back to the graph
            self.addEdge(u, v)

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True

    # Print Euler tour starting from vertex u

    def printEulerUtil(self, u, peso):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                print("%s-%s" % (u, v)),
                for i in self.arestas:
                    if i[0] == str(u+v) or i[0] == str(v+u):
                        peso += i[1]
                        print(peso)

                self.rmvEdge(u, v)
                self.printEulerUtil(v)

    '''The main function that print Eulerian Trail. It first finds an odd
   degree vertex (if there is any) and then calls printEulerUtil()
   to print the path '''

    def printEulerTour(self):
        # Find a vertex with odd degree
        u = 0
        for i in self.V:
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        print("\n")
        peso = 0
        if u == 0:
            self.printEulerUtil(self.V[u], peso)
        else:
            self.printEulerUtil(u, peso)

# Create a graph given in the above diagram


# This code is contributed by Neelam Yadav
