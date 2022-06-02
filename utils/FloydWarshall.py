
from shlex import join


class FloydWarshall():

    def solve(self, Grafo):
        d = self.createCostMatrix(Grafo)
        parents = self.createParentsMatrix(Grafo)
        paths = self.createPathMatrix(Grafo)
        for k in range(len(Grafo.V)):
            for i in range(len(Grafo.V)):
                for j in range(len(Grafo.V)):
                    if i != j:

                        other_path = d[i][k] + d[k][j]

                        if d[i][j] > other_path:
                            d[i][j] = other_path
                            parents[i][j] = k
                        if parents[i][j] not in paths[i][j] and parents[i][j] != 'n':
                            paths[i][j] = [paths[i][j][0]] + paths[k][j]

        for i in range(len(Grafo.V)):
            for j in range(len(Grafo.V)):
                if i != j:
                    paths[i][j].append(j)

        self.printSolution(Grafo, d, paths)

    def createCostMatrix(self, Grafo):
        matrix = [[0 for i in range(len(Grafo.V))]
                  for j in range(len(Grafo.V))]
        edges = [item[0] for item in Grafo.edges]
        for i in range(len(Grafo.V)):
            for j in range(len(Grafo.V)):
                if i != j:
                    if (Grafo.V[i], Grafo.V[j]) not in edges:
                        matrix[i][j] = float('inf')
                    else:
                        matrix[i][j] = Grafo.edges[edges.index(
                            (Grafo.V[i], Grafo.V[j]))][1]
                else:
                    matrix[i][j] = 0
        return matrix

    def createParentsMatrix(self, Grafo):
        matrix = [[0 for i in range(len(Grafo.V))]
                  for j in range(len(Grafo.V))]
        edges = [item[0] for item in Grafo.edges]
        for i in range(len(Grafo.V)):
            for j in range(len(Grafo.V)):
                matrix[i][j] = i if (Grafo.V[i], Grafo.V[j]) in edges else "n"

        return matrix

    def printSolution(self, Grafo, costs, path):
        for i in range(len(Grafo.V)):
            for j in range(len(Grafo.V)):
                print("Distancia de ", (i+1), " para ", (j+1), ": ",
                      costs[i][j], " caminho: ", path[i][j])

    def createPathMatrix(self, Grafo):
        matrix = [[[] for i in range(len(Grafo.V))]
                  for j in range(len(Grafo.V))]
        edges = [item[0] for item in Grafo.edges]
        for i in range(len(Grafo.V)):
            for j in range(len(Grafo.V)):
                if i != j:
                    matrix[i][j].append(i)
                else:
                    matrix[i][j].append(None)
        return matrix

    def constructPath(self, paths, u, v):

        # Storing the path in a vector
        path = [u]
        while (u != v):
            u = paths[u][v]
            path.append(u)

        return path
