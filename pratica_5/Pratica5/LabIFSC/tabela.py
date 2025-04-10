#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from .matematica import soma, sqrt
from .medida import Medida
from copy import copy

class Tabela:
    def __init__(self, colunas=[], titulo='Título', fonte="Autoria própria", maximoDeLinhas = None):
        self._colunas = []
        self._titulo = titulo
        self._fonte = fonte
        self._maximoDeLinhas = None
        pass
    
    def copy(self):
        newColunas = self._colunas.copy()
        newTitulo = self._titulo.copy()
        newFonte = self._fonte.copy()
        newMaximoDeLinhas = self._maximoDeLinhas.copy()
        return Tabela(newColunas, newTitulo, newFonte, newMaximoDeLinhas)

    def addColuna(self, arrayDeMedidas, titulo):
        if(self._maximoDeLinhas):
            assert len(arrayDeMedidas) == self._maximoDeLinhas, f"A nova coluna precisa ter {self._maximoDeLinhas} linhas."

        lastItem = arrayDeMedidas[0]
        unidadesDiferentes = False
        incertezasDiferentes = False

        for index in range(1, len(arrayDeMedidas)):
            item = arrayDeMedidas[index]
            if(item.incerteza != lastItem.incerteza):
                incertezasDiferentes = True
            elif(item.unidade() != lastItem.unidade()):
                unidadesDiferentes = True
        
        assert unidadesDiferentes == False, "Todos os elementos do array de medidas precisam ter a mesma unidade"
        self._maximoDeLinhas = len(arrayDeMedidas)

        stringsColuna = []
        unidadeColuna = f' ({arrayDeMedidas[0].unidade()})'
        incertezaColuna = ''
        for item in arrayDeMedidas:
            currNominal, currIncerteza = '{:-,ifsc}'.format(item).split(' ')[0].replace('(', '').replace(')', '').split('±')
            if(not incertezasDiferentes):
                stringsColuna.append(currNominal.replace('.', ','))
                incertezaColuna = f" $\pm$ {str(currIncerteza).replace('.', ',')}"+unidadeColuna
            else:
                stringsColuna.append(currNominal.replace('.', ',') +"$\pm$"+currIncerteza.replace('.', ','))
                incertezaColuna = ''

        self._colunas.append({'titulo': titulo+unidadeColuna+incertezaColuna, 'dados': stringsColuna})

    def delColuna(self, index):
        try:
            del self._colunas[index]
        except:
            raise Exception('Não existe nenhuma coluna com esse índice')
    
    def gerarLatex(self):
        assert len(self._colunas) > 0, "A tabela precisa ter no mínimo uma coluna"

        self._tabular = '|' + '|'.join(['c' for i in self._colunas]) + '|'
        titles = '&'.join([f"\\textbf\u007b{i['titulo']}\u007d" for i in self._colunas]) + '\\\ \hline\n'

        # revisar essa parte do stringorws
        stringRows = []
        cols = [i['dados'] for i in self._colunas]

        for row in range(len(cols[0])):
            currentRow = []
            for col in range(len(cols)):
                currentRow.append(cols[col][row])
            stringRows.append(currentRow)

        rows = ['&'.join(stringRows[i])+'\\\ \hline\n'  for i in range(len(stringRows))]

        header = "\\begin{table}[H]\n"\
                    "\centering\n"\
                    f"\caption\u007b{self._titulo}\u007d\n"\
                    "\label{yourLabelHere}\n"\
                    f"\\begin\u007btabular\u007d\u007b{self._tabular}\u007d\n"\
                    "\hline\n"
        end =       "\end{tabular}\n"\
                    f"\caption*\u007b{'Fonte: '+self._fonte}\u007d\n"\
                "\end{table}\n"

        completo = header + titles+  ''.join(rows)+end

        return(completo)


def convert_medida_arr_to_nominal(x):
    x_new = []
    for i in x:
        if type(i).__module__ == 'LabIFSC.medida' and type(i).__name__ == 'Medida':
            x_new.append(i.nominal)
        else:
            x_new.append(i)
    return x_new

def media(x, incerteza="desvio padrão"):
    try:
        x = list(x)
    except:
        raise ValueError("x deve ser uma lista ou algo conversível em lista")

    acumulador = copy(x[0])
    acumulador *= 0
    for elemento in x:
        acumulador += elemento
    acumulador /= len(x)

    try:
        avg = copy(acumulador)
        avg.inicializa("0", acumulador.unidades_originais)
    except:
        incerteza = "nenhum"

    avg = copy(acumulador)
    incerteza_val = 0.0
    if incerteza == "nenhum":
        return avg
    elif incerteza == "desvio padrão":
        incerteza_val = desvio_padrao(x)
        avg.inicializa((acumulador.nominal, incerteza_val), acumulador.unidades_originais)
        return avg
    elif incerteza == "propagação":
        return avg
    else:
        raise ValueError("mecanismo de incerteza desconhecido: {}".format(incerteza))


def desvio_padrao(x):
    try:
        x = list(x)
    except:
        raise ValueError("x deve ser uma lista ou algo conversível em lista")

    avg = soma(x)/len(x)

    acumulador = 0.0
    for elemento in x:
        acumulador += (elemento.nominal - avg.nominal)**2
    acumulador /= max(len(x)-1, 1)
    acumulador = math.sqrt(acumulador)
    return acumulador

def linearize(x, y, imprimir=False):
    if type(x[0]).__module__ == 'LabIFSC.medida' and type(x[0]).__name__ == 'Medida':
        x = convert_medida_arr_to_nominal(x)
    if type(y[0]).__module__ == 'LabIFSC.medida' and type(y[0]).__name__ == 'Medida':
        y = convert_medida_arr_to_nominal(y)

    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        raise ValueError("As listas para os valores de 'x' e 'y' tem que ser não nulas ter o mesmo tamanho.")
    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)

    a = sum(list(map(lambda x, y: (x-x_avg)*y, x, y)))
    a /= sum(list(map(lambda x: (x-x_avg)**2, x)))

    b = y_avg - a * x_avg

    dy = sqrt(sum(map(lambda x, y: (a*x + b - y)**2, x, y))/(len(x)-2))

    da = dy/sqrt(sum(map(lambda x: (x-x_avg)**2, x)))

    db = sqrt(sum(map(lambda x: x**2, x))/(len(x)*sum(map(lambda x: (x-x_avg)**2, x)))) * dy

    if imprimir:
        print("a  = {}".format(a))
        print("b  = {}".format(b))
        print("Δy = {}".format(dy))
        print("Δa = {}".format(da))
        print("Δb = {}".format(db))

    return {"a": a, "b": b, "dy": dy, "da": da, "db": db}

# Compara todos os pares (xi, xj) e os retorna em três grupos de acordo com a função de igualdade e desigualdade
def compare(x):
    pass
