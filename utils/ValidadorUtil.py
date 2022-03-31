class ValidadorUtil(object):

    def is_hamiltoniano_Bondy_Chvatal(grafo):
        # A ser corrigido
        newList = []
        nAdjacente = []
        for y in grafo.get_vertices():
            for x in grafo.get_vertices():
                if x not in grafo.get_vertices_adjacentes(y):
                    nAdjacente.append(x)
            nAdjacente.remove(y)

            soma = 0
            for x in nAdjacente:
                soma += grafo.get_grau_vertice(x)

            if soma >= len(grafo.get_vertices()):
                newList.append(1)
            else:
                newList.append(0)
        if 0 in newList:
            return False
        else:
            return True

    def is_hamiltoniano_Ore(grafo):
        vertices = grafo.get_vertices()
        quant_vertices = len(vertices)
        for n in vertices:
            newList = []
            for x in vertices:
                if x not in grafo.get_vertices_adjacentes(n):
                    newList.append(x)
                    current_vertice = n
            newList.remove(n)
            for k in newList:
                if(grafo.get_grau_vertice(current_vertice) + grafo.get_grau_vertice(k) < quant_vertices):
                    return False
        return True

    def is_hamiltoniano_Dirac(grafo):
        newList = []
        if len(grafo.get_vertices()) >= 3:
            for x in grafo.get_vertices():
                if grafo.get_grau_vertice(x) >= len(grafo.get_vertices()) / 2:
                    newList.append(1)
                else:
                    newList.append(0)
        if 0 in newList:
            return False
        else:
            return True

    def is_euleriano(graph):
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

    def exibir_ciclo_euleriano(self, grafo):
        if self.is_euleriano(grafo) == 0:
            return "grafo não-euleriano"
        else:
            if(self.is_euleriano(grafo) == 1):
                vertice = []
                for v in grafo.get_vertices():
                    if grafo.get_grau_vertice(v) % 2 != 0:
                        vertice.append(v)
                for i in vertice:
                    peso = 0
                    lista = []
                    self.percorrer_ciclo(grafo, lista, i, peso)

            else:
                for v in grafo.get_vertices():
                    peso = 0
                    lista = []
                    self.percorrer_ciclo(grafo, lista, v[0], peso)

    def percorrer_ciclo(self, grafo, lista, vertice, peso):
        if len(lista) == len(grafo.get_arestas()):
            print((str(lista) + ', peso: ' + str(peso)))
            return
        else:
            pesoVertice = 0
            for v in grafo.adj[vertice]:
                aresta = str(vertice) + str(v[0])
                if aresta not in lista and aresta[::-1] not in lista:
                    lista.append(aresta)
                    pesoVertice = v[1]
                    peso = peso + pesoVertice
                    self.percorrer_ciclo(grafo, lista, v[0], peso)
                    peso = peso - pesoVertice
            if len(lista) != len(grafo.get_arestas()) and len(lista) > 0:
                lista.pop()
