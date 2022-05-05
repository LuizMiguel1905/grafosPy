from models.grafo import Graph

from queue import PriorityQueue

class Dijsktra:
   
    def __init__(self) -> None:
        pass

    def dijkstra(self, grafo, start_vertex):
        self.visited  = []

        D = {v:float('inf') for v in range(len(grafo.V))}

        D[grafo.V.index(start_vertex)] = 0

        listaP = PriorityQueue()
        listaP.put((0, start_vertex))


        while not listaP.empty():
            (dist, no_atual) = listaP.get()
            self.visited.append(no_atual)
            
            
            for adjacente in grafo.graph[no_atual]:
                for edges, peso in grafo.edges:
                    if edges == (no_atual, adjacente):
                        distance = peso
                        break


                if adjacente not in self.visited:

                    custo_anterior = D[grafo.V.index(adjacente)]
                    novo_custo = D[grafo.V.index(no_atual)] + distance
                    
                    if novo_custo < custo_anterior:
                        
                        listaP.put((novo_custo, adjacente))
                        D[grafo.V.index(adjacente)] = novo_custo

        for no in range(len(D)):
            print("Distância do nó ", start_vertex, " para o nó ", grafo.V[no], "é", D[no])
