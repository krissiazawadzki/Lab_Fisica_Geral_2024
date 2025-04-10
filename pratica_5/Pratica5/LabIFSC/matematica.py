#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from .medida import Medida, MCarlo,montecarlo
import numpy as np
def soma(x):
    try:
        return sum(x)
    except:
        m = Medida(
            (sum(list(map(lambda x: x.nominal, x))),
            sum(list(map(lambda x: x.incerteza, x)))), x[0].unidades_originais)
        return m
def torna_medida(x):
    if not isinstance(x, Medida):
        return Medida(x)
    return x

def AceitaMCarlo(func :callable) -> callable:
    def FuncaoLabificada(*args,**kargs):
        if isinstance(args[0],MCarlo):
            return montecarlo(func,*args,**kargs)
        else:
            return func(*args,**kargs)
    return FuncaoLabificada

sinh=AceitaMCarlo(np.sinh)
cosh=AceitaMCarlo(np.cosh)
tanh=AceitaMCarlo(np.tanh)
arcsinh=AceitaMCarlo(np.arcsinh)
arccosh=AceitaMCarlo(np.arccosh)
arctanh=AceitaMCarlo(np.arctanh)
exp=AceitaMCarlo(np.exp)
exp2=AceitaMCarlo(np.exp2)
sqrt=AceitaMCarlo(np.sqrt)
cbrt=AceitaMCarlo(np.cbrt)
power=AceitaMCarlo(np.power)

    

def cos(x, **kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x, MCarlo):
        x = torna_medida(x)
        nom = math.cos(x.nominal)
        err = math.sin(x.nominal)
        err *= x.incerteza
        return Medida((nom, err), "")
    else:
        import numpy as np
        return AceitaMCarlo(np.cos)(x, **kwargs)

def sin(x,**kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x,MCarlo):
        x    = torna_medida(x)
        nom  = math.sin(x.nominal)
        err  = math.cos(x.nominal)
        err *= x.incerteza
        return Medida((nom, err))
    else:
         import numpy as np
         return AceitaMCarlo(np.sin)(x,**kwargs)
    
def tan(x,**kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x,MCarlo):
        x    = torna_medida(x)
        nom  = math.tan(x.nominal)
        err  = (1.0/math.cos(x.nominal))**2
        err *= x.incerteza
        return Medida((nom, err))
    else:
        import numpy as np
        return AceitaMCarlo(np.tan)(x,**kwargs)
    
def arc_cos(x,**kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x,MCarlo):
        x    = torna_medida(x)
        nom  = math.acos(x.nominal)
        err  = 1/math.sqrt(1 - x.nominal**2)
        err *= x.incerteza
        return Medida((nom, err), "")
    else:
        import numpy as np
        return AceitaMCarlo(np.arccos)(x,**kwargs)
def arc_sin(x,**kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x,MCarlo):
        x    = torna_medida(x)
        nom  = math.asin(x.nominal)
        err  = 1/math.sqrt(1 - x.nominal**2)
        err *= x.incerteza
        return Medida((nom, err), "")
    else:
        import numpy as np
        return AceitaMCarlo(np.arcsin)(x,**kwargs)
    
def arc_tan(x,**kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x,MCarlo):
        x    = torna_medida(x)
        nom  = math.atan(x.nominal)
        err  = 1/math.sqrt(1 - x.nominal**2)
        err *= x.incerteza
        return Medida((nom, err), "")
    else:
        import numpy as np
        return AceitaMCarlo(np.arctan)(x,**kwargs)
    
def log(x, b=math.e,**kwargs):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    if not isinstance(x,MCarlo):
        x    = torna_medida(x)
        nom  = math.log(x.nominal, b)
        err  = math.log(math.exp(1), b)/x.nominal
        err *= x.incerteza
        return Medida((nom, err), x.unidades_originais)
    else:
        import numpy as np
        log_any_base=lambda x: np.log(x)/np.log(b)
        return AceitaMCarlo(log_any_base)(x,**kwargs)
def log2(x):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    return log(x, 2)
def log10(x):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    return log(x, 10)
def ln(x):
    '''Se type(x) == Medida, será usado a propagação de erro do LabIFSC
    
    Se type(x) == MCarlo, Monte Carlo será usado   

    Kwargs:
        Métodos como hist, probabilidade são 
        
        acessíveis usando objetos da classe MCarlo'''
    return log(x, math.exp(1))

def sqrt(x):
    return power(x,1/2)
def cbrt(x):
    return power(x,1.0/3.0)


def dam(x):
    new_arr = []
    for i in x:
        if type(i).__name__ == 'Medida':
            new_arr.append(i.nominal)
        else:
            new_arr.append(i)
    soma = 0
    media = sum(new_arr)/len(new_arr)
    for i in new_arr:
        soma+=abs(i - media)
    
    return soma/len(new_arr)

def mean(x):
    new_arr = []
    for i in x:
        if type(i).__name__ == 'Medida':
            new_arr.append(i.nominal)
        else:
            new_arr.append(i)
    media = sum(new_arr)/len(new_arr)
    return media
__all__ = ["soma","torna_medida","cos", "sin", "tan", "arc_cos", "arc_sin", "arc_tan", 
           "log", "log10", "log2" ,"ln","sqrt", "cbrt", "dam", "mean",
           "sinh","cosh","tanh","arcsinh","arccosh","arctanh","exp","exp2","AceitaMCarlo"]
funcoes_matematicas=__all__