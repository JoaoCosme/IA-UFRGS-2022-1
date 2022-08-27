import numpy as np

def deriva_theta_0(theta_0,theta_1,data):
    somatorio_dos_erros = 0
    for data_entry in data:
        somatorio_dos_erros += calcula_y(theta_0,theta_1,data_entry[0]-data_entry[1])
    return 2*somatorio_dos_erros/len(data)

def deriva_theta_1(theta_0,theta_1,data):
    somatorio_dos_erros = 0
    for data_entry in data:
        somatorio_dos_erros += calcula_y(theta_0,theta_1,data_entry[0]-data_entry[1])*data_entry[0]
    return 2*somatorio_dos_erros/len(data)

def calcula_y(theta_0,theta_1,x):
    return theta_0 + theta_1 * x

def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    somatorio_dos_quadrados = 0
    for data_entry in data:
        somatorio_dos_quadrados += pow(calcula_y(theta_0,theta_1,data_entry[0]) - data_entry[1],2)
    return somatorio_dos_quadrados/len(data)


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    return theta_0 - alpha*deriva_theta_0(theta_0,theta_1,data),theta_1 - alpha*deriva_theta_1(theta_0,theta_1,data)

def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    raise NotImplementedError  # substituir pelo seu codigo
