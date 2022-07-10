from heapq import heapify, heappop, heappush
import queue
from typing import Dict, List
from nodo import Nodo


class Lista_Prio_Nodo(object):
    def __init__(self):
        self.queue = []
        heapify(self.queue)
        
    def append(self,nodo:Nodo):
        heappush(self.queue,nodo)
        
    def __len__(self):
        return len(self.queue)
 
    # for inserting an element in the queue
    def extend(self, lista_nodos:List):
        for nodo in lista_nodos:
                self.append(nodo)
 
    # for popping an element based on Priority
    def pop(self):
        return heappop(self.queue)
