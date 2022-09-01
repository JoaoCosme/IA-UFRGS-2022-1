# Trabalho 3 - Otimização

# IA 2022/1 - GRUPO 5

|Nome|Cartao|Turma|
|---|---|----|
|Alice Santin Varella| 00259915 | B 
|Joao Pedro Cosme da Silva|00314792 |A
|Eduardo André Leite | 00287684| A

## Algoritmo Genético

Um do conjuntos de valores que consegue atingir a execução bem sucedida (0 Ataques):
-> g:int (Número de gerações) = 20
-> n:int (Número de indivíduos) = 10
-> k:int (Número de participantes do torneio) = 2
-> m:float (Probabilidade de mutação (entre 0 e 1)) = 0.5 
-> e:bool (Verdadeiro se há elitismo) = True 

Menor número de ataques = 0.

## Regressão Linear

Melhor run:

```python
theta_0s, theta_1s = alegrete.fit(
    quiz_data, theta_0=random.randint(-100,100), theta_1=random.randint(-100,100), 
    alpha=0.01, num_iterations=1000
)
```
