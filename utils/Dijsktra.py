from models.grafo import Graph

from queue import PriorityQueue


class Dijsktra:

    def __init__(self) -> None:
        pass

    def dijkstra(self, grafo):
        for v in grafo.V:
            self.visited = []

            D = {v: float('inf') for v in range(len(grafo.V))}

            D[grafo.V.index(v)] = 0
            paths = ["Caminho: " + v] * len(grafo.V)
            listaP = PriorityQueue()
            listaP.put((0, v))

            while not listaP.empty():
                (dist, no_atual) = listaP.get()
                self.visited.append(no_atual)

                for adjacente in grafo.graph[no_atual]:
                    caminho = ""
                    for edges, peso in grafo.edges:
                        if edges == (no_atual, adjacente):
                            caminho = "-> " + adjacente
                            distance = peso
                            break

                    if adjacente not in self.visited:

                        custo_anterior = D[grafo.V.index(adjacente)]
                        novo_custo = D[grafo.V.index(no_atual)] + distance
                        novo_caminho = paths[grafo.V.index(no_atual)] + caminho
                        if novo_custo < custo_anterior and novo_custo < D[grafo.V.index(adjacente)]:

                            paths[grafo.V.index(
                                adjacente)] = novo_caminho
                            listaP.put((novo_custo, adjacente))
                            D[grafo.V.index(adjacente)] = novo_custo

            for no in range(len(D)):
                path = ''
                if D[no] != path:
                    path = paths[no]
                print("Distância do nó ", v,
                      " para o nó ", grafo.V[no], "é", D[no], " ", path)
            print("##############################################")
