class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:object, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


class busca_grafo:
    """
    Classe que possui a estrutura geral do algoritmo de busca. Recebe o algoritmo que implementa a fronteira.
    """
    def __init__(self,func_desempilha):
        self.func_desempilha = func_desempilha
    def busca_grafo(nodo):
        raise NotImplementedError



def cria_nodo(estado, pai, acao, custo):
    return Nodo(estado, pai, acao, custo)
                        
def sucessor(estado):
    acoes_possiveis = []
    indice = estado.find('_')
    if pode_mover_abaixo(indice):
        acoes_possiveis.append("abaixo")
    if pode_mover_acima(indice):
        acoes_possiveis.append("acima")
    if pode_mover_direita(indice):
        acoes_possiveis.append("direita")
    if pode_mover_esquerda(indice):
        acoes_possiveis.append("esquerda")
    return determina_estados(acoes_possiveis, estado, indice)
    
'''Funções auxiliares da função sucessor:
ação direita: swap [i] com [i+1] || pode ir para direita se índice != 2, != 5 != 8
ação esquerda: swap [i] com [i-1] || pode ir para esquerda se índice != 0, != 3, != 6
ação cima: swap [i] com [i-3] || pode mover para cima quando índice > 2
ação baixo: swap[i] com [i+3] || pode mover para baixo quando índice < 6
'''
#funções que encontram movimentos possíveis:
def pode_mover_direita(indice):
    if indice not in (2,5,8):
        return True
    else:
        return False

def pode_mover_esquerda(indice):
    if indice not in (0,3,6):
        return True
    else:
        return False

def pode_mover_abaixo(indice):
    if indice < 6:
        return True
    else:
        return False

def pode_mover_acima(indice):
    if indice > 2:
        return True
    else:
        return False

#cria estados atualizados
def novo_estado(estado, indice, novo_indice):
    prox_estado = list(estado)
    prox_estado[indice], prox_estado[novo_indice] = prox_estado[novo_indice], prox_estado[indice]
    return ''.join(prox_estado)

#cria tuplas de sucessores
def determina_estados(acoes_possiveis, estado, indice):
    sucessores = []
    for acao in acoes_possiveis:
        if acao == "direita":
            sucessores.append((acao, novo_estado(estado, indice, indice+1)))
        elif acao == "esquerda":
            sucessores.append((acao, novo_estado(estado, indice, indice-1)))
        elif acao == "acima":
            sucessores.append((acao, novo_estado(estado, indice, indice-3)))
        elif acao == "abaixo":
            sucessores.append((acao, novo_estado(estado, indice, indice+3)))
    return sucessores

def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
