
from models.grafo import Graph


class PathUtil(object):

    def __init__(self):
        self.graph = None

    def CreateSpanningTreeBFS(self, grafo, rootnode):
        color = ['white'] * len(grafo.V)
        distance = [0] * len(grafo.V)
        parent = [""] * len(grafo.V)
        RootIndex = grafo.V.index(rootnode)
        color[RootIndex] = 'gray'
        distance[RootIndex] = 0
        Q = []
        Q.append(rootnode)
        Arvore = Graph()
        Arvore.addVertices(grafo.V)
        while Q:
            u = Q.pop()
            for v in grafo.graph[u]:
                if color[grafo.V.index(v)] == 'white':
                    color[grafo.V.index(v)] = 'gray'
                    distance[grafo.V.index(v)] += 1
                    parent[grafo.V.index(v)] = u
                    Arvore.addEdge(Arvore.V[grafo.V.index(v)], u)
                    Q.append(v)
            color[grafo.V.index(u)] = 'black'
        print("Distancia de todos os vértices até a raiz em ordem alfabética dos vértices " + str(distance))
        return Arvore

    def CreateSpanningTreeDFSRecursive(self, grafo, rootnode):
        self.graph = grafo
        Arvore = Graph()
        Arvore.addVertices(grafo.V)
        visited = [False]*(len(Arvore.V))
        self.DFS(Arvore.V.index(rootnode), visited, Arvore)
        return Arvore

    def DFS(self, v, visited, Arvore):
        visited[v] = True
        for i in self.graph[self.graph.V[v]]:
            if visited[self.graph.V.index(i)] == False:
                Arvore.addEdge(self.graph.V[v], i)
                self.DFS(self.graph.V.index(i), visited, Arvore)

    def CreateSpanningTreeDFSStack(self, grafo, rootnode):
        Arvore = Graph()
        Arvore.addVertices(grafo.V)
        visited = [False]*(len(Arvore.V))
        parent = [""]*(len(Arvore.V))
        pilha = list()
        pilha.append(rootnode)
        while pilha:
            u = pilha.pop()
            if visited[Arvore.V.index(u)] == False:
                visited[Arvore.V.index(u)] = True
                print(u + " ")
                for v in grafo.graph[u][::-1]:
                    pilha.append(v)
                    parent[grafo.V.index(v)] = u
                if parent[grafo.V.index(u)] != "":
                    Arvore.addEdge(parent[grafo.V.index(u)], u)

        return Arvore

    def CreateSpanningTreeDFSStack2(self, grafo, rootnode):
        Arvore = Graph()
        Arvore.addVertices(grafo.V)
        visited = [False]*(len(Arvore.V))
        pilha = list()
        pilha.append(rootnode)
        ultimoNo = ""
        while pilha:
            u = pilha.pop()
            if visited[Arvore.V.index(u)] == False:
                visited[Arvore.V.index(u)] = True
                for v in grafo.graph[u][::-1]:
                    pilha.append(v)
                    ultimoNo = v
                if ultimoNo != "":
                    Arvore.addEdge(ultimoNo, u)

        return Arvore

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[self.graph.V[v]]:
            if visited[self.graph.V.index(i)] == False:
                count = count + self.DFSCount(self.graph.V.index(i), visited)
        return count

    def isValidNextEdgeDFS(self, u, v):

        if len(self.graph.graph[u]) == 1:
            return True
        else:

            visited = [False]*(len(self.graph.V))
            count1 = self.DFSCount(self.graph.V.index(u), visited)

            self.graph.rmvEdge(u, v)
            visited = [False]*(len(self.graph.V))
            count2 = self.DFSCount(self.graph.V.index(u), visited)

            self.graph.addEdge(u, v)
            return False if count1 > count2 else True

    def printEulerUtil(self, u, peso, caminho):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
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

    def printEulerTour(self, graph):
        self.graph = graph
        u = 0
        for i in graph.V:
            if len(graph.graph[i]) % 2 != 0:
                u = i
                break
        print("\n")
        peso = 0
        caminho = []
        if u == 0:
            self.printEulerUtil(graph.V[u], peso, caminho)
        else:
            self.printEulerUtil(u, peso, caminho)
