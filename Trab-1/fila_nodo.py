from typing import List
from nodo import Nodo


class Lista_Prio_Nodo(object):
    def __init__(self):
        self.queue:List[Nodo] = []
        
    def append(self,data):
        self.queue.append(data)
        
    def __len__(self):
        return len(self.queue)
 
    # for inserting an element in the queue
    def extend(self, data):
        self.queue.extend(data)
 
    # for popping an element based on Priority
    def pop(self):
        min_custo = 1000
        nodo = None
        for i in range(len(self.queue)):
            if self.queue[i].custo_manhattan < min_custo:
                min_custo = self.queue[i].custo_manhattan
                nodo = self.queue[i]
        self.queue.remove(nodo)
        return nodo
