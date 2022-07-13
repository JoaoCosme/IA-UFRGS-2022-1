from heapq import heapify, heappop, heappush
from typing import  List
from nodo import Nodo


class Lista_Prio_Nodo(object):
    """
    Classe que implementa uma queue com min heap para que possa ser utilizada nas
    pesquisas A* para aumento de eficiencia
    """    
    def __init__(self):
        self.queue = []
        heapify(self.queue)
        
    def append(self,nodo:Nodo):
        heappush(self.queue,nodo)
        
    def __len__(self):
        return len(self.queue)
 
    def extend(self, lista_nodos:List):
        for nodo in lista_nodos:
                self.append(nodo)
 
    def pop(self):
        return heappop(self.queue)
