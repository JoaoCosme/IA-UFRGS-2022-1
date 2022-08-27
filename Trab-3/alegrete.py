COORDENADA_X = 0
COORDENADA_Y = 1
VALOR_CALCULADO = 2 

def deriva_theta_0(erros_por_cordenada):
    somatorio_dos_erros = 0
    for erro_por_coordenada in erros_por_cordenada:
        somatorio_dos_erros += erro_por_coordenada[VALOR_CALCULADO]
    return 2*somatorio_dos_erros/len(erros_por_cordenada)

def deriva_theta_1(erros_por_cordenada):
    somatorio_dos_erros = 0
    for erro_por_coordenada in erros_por_cordenada:
        somatorio_dos_erros += erro_por_coordenada[VALOR_CALCULADO] * erro_por_coordenada[COORDENADA_X]
    return 2*somatorio_dos_erros/len(erros_por_cordenada)

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

def calcula_erros_por_cordenada(theta_0,theta_1,data):
    valor_por_cordenada = []
    quantidade_de_dados = len(data)
    for i in range(quantidade_de_dados):
        estimativa_calculada = calcula_y(theta_0,theta_1,data[i][COORDENADA_X]) - data[i][COORDENADA_Y]
        valor_por_cordenada.append([data[i][COORDENADA_X],data[i][COORDENADA_Y],estimativa_calculada])
    return valor_por_cordenada

def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    erros_por_cordenada = calcula_erros_por_cordenada(theta_0,theta_1,data)
    return theta_0 - alpha*deriva_theta_0(erros_por_cordenada),theta_1 - alpha*deriva_theta_1(erros_por_cordenada)

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
