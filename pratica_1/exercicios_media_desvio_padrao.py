'''
    Esse código lê um arquivo de dados e a precisão do instrumento
    e calcula a média, desvio padrão, desvio médio.
    Ao final, retorna a medida final, considerando os desvios e 
    precisão com o número de algarismos significativos apropriados

'''
# biblioteca numerica do python
import numpy as np
# biblioteca de algarismos significativos do python
from sigfig import round


import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-p','--precisao_instrumento', type=float, default=None, help='Precisão do instrumento')
parser.add_argument('-u','--unidade_de_medida', type=str, default='mm', help='Unidade de medida')
parser.add_argument('-a','--arquivo_dados', type=str, default='dados_exemplo.txt', help='Nome do arquivo onde estão salvos os dados em uma única coluna.')


opts = parser.parse_args()

precisao_instrumento = opts.precisao_instrumento
unidade_de_medida = opts.unidade_de_medida
arquivo_dados = opts.arquivo_dados




x_i = np.loadtxt(arquivo_dados)
N = x_i.shape[0]

# determina a precisao de acordo com o digito mais à direita
precisao = len(str(x_i[0]).split('.')[1])
if(precisao_instrumento is None):
    for i in range(1,N):
        p_i = len(str(x_i[i]).split('.')[1])
        precisao = np.max([precisao, p_i])

d_instrumento = 1./(10**precisao)
# média dos x_i
x_m = x_i.sum() / N

# desvio padrao
d_padrao = np.sqrt(((x_i - x_m)**2).sum() / (N-1))

# desvio medio
d_medio = (np.abs(x_i - x_m)).sum() / N
x_std = x_i.std()

print(f'-> x médio (s/arredondamentos): {x_m} {unidade_de_medida}')
print("")
print(f'-> desvio médio (s/arredondamentos): {d_medio} {unidade_de_medida}')
print(f'-> desvio padrão (s/arredondamentos): {d_padrao} {unidade_de_medida}')

d_medio_sig = round(d_medio, sigfigs=1)
d_padrao_sig = round(d_padrao, sigfigs=1)

print("")
print(f'-> desvio médio (1 algarismo significativo): {d_medio_sig} {unidade_de_medida}')
print(f'-> desvio padrão (1 algarismo significativo): {d_padrao_sig} {unidade_de_medida}')

d_final = np.max([d_medio_sig, d_padrao_sig, d_instrumento])
print(f'-> maior dos desvios (1 algarismo significativo): {d_final} {unidade_de_medida}')

print("")
print(f'-> desvio médio (1 algarismo significativo): {d_medio_sig} {unidade_de_medida}')
print(f'-> desvio padrão (1 algarismo significativo): {d_padrao_sig} {unidade_de_medida}')


medida_dpadrao_sig = round(str(x_m), str(d_padrao_sig))
medida_medio_sig = round(str(x_m), str(d_medio_sig))
medida_final_sig = round(str(x_m), str(d_final))

print("")
print(f'-> medida final (desvio padrão): ({medida_dpadrao_sig}) {unidade_de_medida}')
print(f'-> medida final (desvio médio): ({medida_medio_sig}){unidade_de_medida}')

print(f'-> medida final (maior desvio): ({medida_final_sig}) {unidade_de_medida}')