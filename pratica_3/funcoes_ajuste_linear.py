import numpy as np

'''
    Função auxiliar para ler dados
'''
def le_dados(nome_arquivo_dados:str):
    '''
        le_dados

        Inputs:
        nome_arquivo_dados: nome do arquivo onde os dados estão armazenados
            (x_i, y_i) é uma linha

        Ouputs:
        x_i: vetor coluna com dados x_i (np.array)
        y_i: vetor coluna com dados y_i (np.array)
        N: número de dados lidos
    '''

    # lendo o arquivo
    dados = np.loadtxt(nome_arquivo_dados, delimiter=',')

    # organizando os x_i e y_i em variáveis separadas
    x_i = dados[:,0]
    y_i = dados[:,1]

    # pega o número de dados automaticamente
    N = x_i.shape[0]

    return x_i, y_i, N

'''
    Ajuste linear com numpy
'''
def ajuste_linear_bf(x_i:np.array, y_i:np.array, N:int):
    '''
        ajuste_linear_bf

        Inputs:
            x_i: valores dos dados x (np.array)
            y_i: valores dos dados y (np.array)
            N: número de pontos
    '''
    # somas
    Sx = x_i.sum()
    Sy = y_i.sum()
    Sxx = (x_i * x_i).sum()
    Sxy = (x_i * y_i).sum()
    Syy = (y_i * y_i).sum()

    # valores médios
    y_m = Sy / N
    x_m = Sx / N

    # cálculo dos coeficientes
    b = (Sxy * N - Sy * Sx) / (Sxx * N - Sx**2)
    a = y_m - b * x_m

    # valores y_Ci para o modelo
    y_Ci = a + b * x_i

    # distância quadrada dos pontos y_i com os do modelo y_Ci
    r_i = y_i - y_Ci

    # estimador da variância
    Delta_y = np.sqrt((r_i**2).sum() / (N-2))

    # erro nos coeficientes
    Delta_b = Delta_y / np.sqrt(Sxx-Sx**2 / N)
    Delta_a = Delta_b * np.sqrt(Sxx / N)


    # R quadrado
    R2 = 1 - Delta_y**2 * (N-2) / ((y_i - y_m)**2).sum()

    return [a,b], [Delta_a, Delta_b], R2


'''
    Ajuste linear com scipy e R2 com sklearn
'''
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


# modelo linear
def modelo_linear(x, b:float, a:float):
    '''
        modelo_linear

        Inputs:
        x: variável independente
        a: coeficiente linear
        b: coeficiente angular
    '''
    return b*x + a

def ajuste_linear_pl(x_i:np.array, y_i:np.array, N:int):
    '''
        ajuste_linear_pl

        Inputs:
            x_i: valores dos dados x (np.array)
            y_i: valores dos dados y (np.array)
            N: número de pontos
    '''

    coefs_lin, cov_lin = curve_fit(modelo_linear, x_i, y_i)
    coefs_err = np.sqrt(np.diag(cov_lin))

    # cálculo dos coeficientes: aqui a ordem é a mesma em que eles aparecem na função
    b = coefs_lin[0]
    a = coefs_lin[1]

    # valores y_Ci para o modelo
    y_Ci = a + b * x_i

    # erro nos coeficientes
    Delta_b = coefs_err[0]
    Delta_a = coefs_err[1]


    # R quadrado
    R2 = r2_score(y_Ci, y_i)

    return [a,b], [Delta_a, Delta_b], R2
