from constantes import HAMMING, MANHATTAN, ESTADO_FINAL
from operator import lt
from typing import List, Optional
from manhattan import calcula_distancia_manhattan
from hamming import calcula_distancia_hamming

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai=None, acao:str=None, custo:int=0, astar:str=None):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai:Nodo = pai
        self.acao = acao
        self.custo = custo
        self.custo_astar = self.calcula_distancia_escolhida(astar)+custo
        
    def calcula_distancia_escolhida(self,astar:str):
        if astar == MANHATTAN:
            return calcula_distancia_manhattan(self.estado,self.custo)
        elif astar == HAMMING:
            return calcula_distancia_hamming(self.estado,ESTADO_FINAL)
        else:
            return self.custo
        
    def __lt__(self,other):
        return self.custo_astar < other.custo_astar

    def retorna_caminho(self,caminho:Optional[List]=None):
        caminho = caminho or []
        if self.pai: 
            caminho.append(self.acao)          
            return self.pai.retorna_caminho(caminho) 
        else: 
            caminho.reverse()
            return caminho
