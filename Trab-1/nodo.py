from typing import List


List

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:any=None, acao:str=None, custo:int=0):
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
    def retorna_caminho(self,caminho:List=None):
        if self.pai: 
            if caminho:
                caminho.append(self.acao)
            else:
                caminho = [self.acao]            
            return self.pai.retorna_caminho(caminho) 
        else: 
            caminho.reverse()
            return caminho
