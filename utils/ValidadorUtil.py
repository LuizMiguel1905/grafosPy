class ValidadorUtil(object):

    def isHamiltonianoBondyChvatal(grafo):
        # A ser corrigido
        newList = []
        nAdjacente = []
        for y in grafo.V:
            for x in grafo.V:
                if x not in grafo.getAdjVertices(y):
                    nAdjacente.append(x)
            nAdjacente.remove(y)

            soma = 0
            for x in nAdjacente:
                soma += grafo.getVerticeDegree(x)
            newList.append(1) if soma >= len(grafo.V) else newList.append(0)

        return False if 0 in newList else True

    def isHamiltonianoOre(grafo):
        quant_vertices = len(grafo.V)
        for n in grafo.V:
            newList = []
            for x in grafo.V:
                if x not in grafo.getAdjVertices(n):
                    newList.append(x)
                    current_vertice = n
            newList.remove(n)
            for k in newList:
                if(grafo.getVerticeDegree(current_vertice) + grafo.getVerticeDegree(k) < quant_vertices):
                    return False
        return True

    def isHamiltonianDirac(grafo):
        newList = []
        if len(grafo.V) >= 3:
            for x in grafo.V:
                if grafo.getVerticeDegree(x) >= len(grafo.V) / 2:
                    newList.append(1)
                else:
                    newList.append(0)
        if 0 in newList:
            return False
        else:
            return True

    def isEulerian(graph):
        newList = []
        imparCount = 0
        for x in graph.V:
            if len(graph.graph[x]) % 2 == 0:
                newList.append(1)
            else:
                newList.append(0)
                imparCount = imparCount + 1

        if (0 in newList and imparCount == 2):
            return 1
        elif (1 in newList and imparCount == 0):
            return 2
        else:
            return 0
