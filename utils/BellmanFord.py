

class BelmanFord():

    def solve(self, Grafo, rootnode):
        distance = [float('inf')] * len(Grafo.V)
        predecessor = {v: None for v in range(len(Grafo.V))}
        distance[Grafo.V.index(rootnode)] = 0

        for v in range(len(Grafo.V) - 1):
            for edge, weight in Grafo.edges:
                v = Grafo.V.index(edge[1])
                u = Grafo.V.index(edge[0])
                if distance[v] > distance[u] + weight:
                    distance[v] = distance[u] + weight
                    predecessor[v] = edge[0]
        for edge, weight in Grafo.edges:
            if distance[Grafo.V.index(edge[1])] > distance[Grafo.V.index(edge[0])] + weight:

                distance[Grafo.V.index(edge[1])] = float('-inf')

        for i in range(len(distance)):
            print(Grafo.V[i], ": ", distance[i], " caminho: ", self.getPath(Grafo, Grafo.V[i], predecessor)) if distance[i] != 0 and distance[i] != float(
                '-inf') else print(Grafo.V[i], ": ", distance[i], ": não possui caminho")

    def getPath(self, Grafo, vertice, predecessor):
        current = vertice
        caminho = []
        while current != None:
            caminho.insert(0, current)
            current = predecessor[Grafo.V.index(current)]
        return caminho
