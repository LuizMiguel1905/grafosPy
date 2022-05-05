
from models.grafo import Graph

from queue import PriorityQueue

class Dijsktra:
    def __init__(self, quant_de_nos):
        grafo = Graph()
        

        #Numero de vertices
        
        self.v = quant_de_nos

        self.edge = [
            [-1 for i in range(quant_de_nos)] 
            
            for j in range(quant_de_nos)
            ] 
        
        #Vertices visitados
        self.visited = [] 

    #Adicionar as arestas com seus respectivos pesos
    def add_edge(self, u, v, weight):
        self.edge[u][v] = weight
        self.edge[v][u] = weight
    
    def dijkstra(self, start_vertex):

        
        #Criar uma lista D de tamanho V
        D = {v:float('inf') for v in range(self.v)}

        D[start_vertex] = 0

        #Lista de prioridade
        listaP = PriorityQueue()
        listaP.put((0, start_vertex))

        #Loop só acabara quando todos os nós estiverem em D
        while not listaP.empty():
            (dist, no_atual) = listaP.get()
            self.visited.append(no_atual)

            #Loop para percorrer todos os nós
            for adjacente in range(self.v):
                if self.edge[no_atual][adjacente] != -1:
                    distance = self.edge[no_atual][adjacente]
                    #Caso o nó adjacente não for visitado
                    if adjacente not in self.visited:

                        
                        custo_anterior = D[adjacente]
                        novo_custo = D[no_atual] + distance


                        #Caso o ó antigo seja maior que o novo
                        #O custo nnovo sera adicionado a
                        if novo_custo < custo_anterior:

                            listaP.put((novo_custo, adjacente))
                            D[adjacente] = novo_custo
        return D

g = Dijsktra(6)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 1)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(2, 3, 3)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 1)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 2)

D = g.dijkstra(0)

for no in range(len(D)):
    print("Distância do nó 0 para o nó", no, "é", D[no])
