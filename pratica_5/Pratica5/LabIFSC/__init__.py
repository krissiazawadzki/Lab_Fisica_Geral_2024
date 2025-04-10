#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gabriel Queiroz"
__credits__ = ["gabriel Queiroz", "Pedro Ilídio"]
__license__ = "MIT"
__version__ = "0.1.13"
__email__ = "gabrieljvnq@gmail.com"
__status__ = "Production"

num_gaussianos=int(1e5)    
def quantidade_numeros_gaussianos(valor):
    try: valor=int(valor)
    except:
        raise ValueError("Esse objeto não pode ser convertido em inteiro")
    global num_gaussianos
    num_gaussianos=valor

from .geral import TODAS_AS_UNIDADES, MAPA_DE_DIMENSOES, PREFIXOS_SI_LONGOS, PREFIXOS_SI_CURTOS, PREFIXOS_SI, analisa_numero, analisa_unidades, calcula_dimensao, parse_dimensions, acha_unidade, unidades_em_texto
from .medida import Medida, M, arrayM, MCarlo, montecarlo, getIncerteza, getNominal
from .unidade import Unidade
from .lista_de_unidades import registra_unidades ; registra_unidades()
from .matematica import *; from .matematica import funcoes_matematicas
from .tabela import media, desvio_padrao, linearize, compare, Tabela
from .constantes import *


__all__ = [
    "TODAS_AS_UNIDADES", "MAPA_DE_DIMENSOES", "PREFIXOS_SI_LONGOS", "PREFIXOS_SI_CURTOS", "PREFIXOS_SI", "analisa_numero", "analisa_unidades", "calcula_dimensao", "parse_dimensions", "acha_unidade", "unidades_em_texto",
    "Medida", "M","MCarlo", "arrayM", "Tabela","getIncerteza","getNominal",
    "Unidade",
    "registra_unidades", "media", "desvio_padrao", "linearize", 
    "compare","montecarlo","quantidade_numeros_gaussianos"] + nomes_constantes + funcoes_matematicas
