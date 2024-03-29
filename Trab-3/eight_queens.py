from functools import reduce
from typing import List, Tuple
import random

MAX = 1000


def evaluate(individual:List[int])->List[int]:
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    len_individuos = len(individual)
    conflitos = [0] * len_individuos
    
    detecta_conflito = lambda i,j,deslocamento: individual[i] == individual[j] + deslocamento
    na_mesma_linha = lambda i,j : detecta_conflito(i,j,0)
    na_diagonal_superior = lambda i,j : detecta_conflito(i,j,i-j)
    na_diagonal_inferior = lambda i,j : detecta_conflito(i,j,j-i)
    
    for i in range(len_individuos):
        for j in range(i+1,len_individuos):
            if na_mesma_linha(i,j):
                conflitos[i]+=1
            elif na_diagonal_superior(i,j) or na_diagonal_inferior(i,j):
                conflitos[i]+=1
            
    return reduce(lambda total,conflito_atual : total+conflito_atual,conflitos)

def tournament(participants:List[List[int]])->List[int]:
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    
    melhor = (MAX,[])
    for participante in participants:
        nota = evaluate(participante)
        if nota < melhor[0]:
            melhor = (nota,participante)

    return melhor[1]


def crossover(parent1:List, parent2:List, index:int)->Tuple[List,List]:
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    filho1 = []
    filho2 = []
    
    for i in range(index):
        filho1.append(parent1[i])
        filho2.append(parent2[i])
        
    for i in range(i+1,len(parent1)):
        filho1.append(parent2[i])
        filho2.append(parent1[i])
    
    return filho1,filho2
   


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    novo_individuo = individual.copy() #copia da lista de entrada
    if random.random() < m:
        mutacao = random.randint(1,8)  #sorteia numero aleatorio da mutacao
        posicao_sorteada = random.randint(0,7) #sorteia posicao onde ocorre a mutacao
        novo_individuo[posicao_sorteada] = mutacao
        return novo_individuo  #retorna lista onde foi efetuada a mutacao
    return individual



def first_gen(n): #cria primeira geracao com n individuos distintos
    generation_one = []
    population_counter = 0
    while population_counter < n:
        new_individual = []
        for i in range(8):
            new_individual.append(random.randint(1,8))
        if new_individual not in generation_one: #garante que cada individuo adicionado eh diferente dos demais
            generation_one.append(new_individual)
            population_counter += 1
    return generation_one


def tournament_participants(current_generation, k): #seleciona k individuos da geracao atual aleatoriamente para participar do torneio
    participants = []
    while len(participants) < k:
        individual_index = random.randint(0, (len(current_generation)-1)) #sorteia indice do individuo
        if current_generation[individual_index] not in participants: #garante que o mesmo participante nao sera adicionado duas vezes
            participants.append(current_generation[individual_index])
    return participants



def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    current_generation = first_gen(n)
    count_generations = 0
    while count_generations < g:
        next_generation = []
        if e is True: #se tem elitismo, o melhor da geracao atual passara para a proxima geracao
            next_generation.append(tournament(current_generation))
        while len(next_generation) < n: #execucao do algoritmo genetico conforme visto em aula.
            p1 = tournament(tournament_participants(current_generation, k))
            p2 = tournament(tournament_participants(current_generation, k))
            o1,o2 = crossover(p1, p2, random.randint(1,7))
            o1 = mutate(o1, m)
            o2 = mutate(o2, m)
            next_generation.append(o1)
            next_generation.append(o2)
        current_generation = next_generation #geracao criada neste loop sera a geracao atual do proximo loop
        count_generations += 1
    
    best_of_last_gen = tournament(current_generation)
    return best_of_last_gen