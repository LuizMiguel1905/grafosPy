class PathUtil(object):

    def __init__(self):
        self.graph = None

    def BFS(grafo, rootnode):
        color = ('white') * len(grafo.V)
        distance = (10000000) * len(grafo.V)
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
                    parent[grafo.V.index(v)] = u
            color[grafo.V.index(u)] = 'black'

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[self.graph.V[v]]:
            if visited[self.graph.V.index(i)] == False:
                count = count + self.DFSCount(self.graph.V.index(i), visited)
        return count

    # The function to check if edge u-v can be considered as next edge in
    # Euler Tour
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:

        #  1) If v is the only adjacent vertex of u
        if len(self.graph.graph[u]) == 1:
            return True
        else:
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge

            2.a) count of vertices reachable from u'''
            visited = [False]*(len(self.graph.V))
            count1 = self.DFSCount(self.graph.V.index(u), visited)

            '''2.b) Remove edge (u, v) and after removing the edge, count
                vertices reachable from u'''
            self.graph.rmvEdge(u, v)
            visited = [False]*(len(self.graph.V))
            count2 = self.DFSCount(self.graph.V.index(u), visited)

            # 2.c) Add the edge back to the graph
            self.graph.addEdge(u, v)

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True

    # Print Euler tour starting from vertex u

    def printEulerUtil(self, u, peso, caminho):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                print("%s-%s" % (u, v)),
                for aresta, custo in self.graph.edges:
                    if aresta == str(u+v) or aresta == str(v+u):
                        peso += custo
                        caminho.append(aresta)
                        if len(caminho) == len(self.graph.edges):
                            print("peso: " + str(peso))
                        break
                self.graph.rmvEdge(u, v)
                self.printEulerUtil(v, peso, caminho)

    '''The main function that print Eulerian Trail. It first finds an odd
   degree vertex (if there is any) and then calls printEulerUtil()
   to print the path '''

    def printEulerTour(self, graph):
        # Find a vertex with odd degree
        self.graph = graph
        u = 0
        for i in graph.V:
            if len(graph.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        print("\n")
        peso = 0
        caminho = []
        if u == 0:
            self.printEulerUtil(graph.V[u], peso, caminho)
        else:
            self.printEulerUtil(u, peso, caminho)
