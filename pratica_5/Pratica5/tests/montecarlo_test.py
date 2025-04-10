import pytest
import math
import numpy as np
from LabIFSC import *
def test_funcoesnativas_MCarlo_vs_Medida(): 
  import numpy as np
  a=Medida((1,0.1))
  b=Medida((2,0.05))
  a_carlo=MCarlo((1,0.1))
  b_carlo=MCarlo((2,0.05))
  assert a_carlo+b_carlo==a+b
  assert a_carlo-b_carlo==a-b
  assert a_carlo*b_carlo==a*b
  assert a_carlo/b_carlo==a/b
  m1=Medida((20,1.5)); m1_c=MCarlo((20,1.5))
  assert cos(m1_c)==cos(m1)
  assert sin(m1_c)==sin(m1)
  assert tan(m1_c)==tan(m1)
  m1=Medida((0.4,0.01)); m1_c=MCarlo((0.4,0.01))
  assert arc_cos(m1_c)==arc_cos(m1)
  assert arc_sin(m1_c)==arc_sin(m1)
  assert arc_tan(m1_c)==arc_tan(m1)
  m1=Medida((1.2,0.01)); m1_c=MCarlo((1.2,0.01))
  assert log2(m1_c)==log2(m1)
  assert log10(m1_c)==log10(m1)



def test_wrongvariables():
  a=MCarlo((7,0.3))
  b=MCarlo((1,0.1))
  statements=[lambda: montecarlo(lambda x:x,3),
              lambda: montecarlo(lambda x:x,3.13),  
              lambda: montecarlo(lambda x:x,"string"),
              lambda: montecarlo(lambda x,y:x+y,[a,b]),
              lambda: montecarlo(lambda x:x,a,probabilidade=3),
              lambda: montecarlo(lambda x:x,a,probabilidade=5.1),
              lambda: montecarlo(lambda x:x,a,hist="True"),
              lambda: montecarlo(lambda x:x,a,hist="False"),
              lambda: montecarlo(a)] 
  for index, statement in enumerate(statements):
    with pytest.raises(TypeError):
     print(index)
     statement()


def test_probabilidade(): #68-95-99.7 rule
  from math import isclose
  from random import random
  quantidade_numeros_gaussianos(int(1e5))
  for _ in range(10):
      media, sigma=random(),random() #gaussianas aleatorias
      a=MCarlo((media,sigma))
      assert isclose(montecarlo(lambda x:x, a,probabilidade=[media-sigma,media+sigma]),0.68,abs_tol=0.02)
      assert isclose(montecarlo(lambda x:x, a,probabilidade=[media-2*sigma,media+2*sigma]),0.95,abs_tol=0.02)
      assert isclose(montecarlo(lambda x:x, a,probabilidade=[media-3*sigma,media+3*sigma]),0.997,abs_tol=0.01)
      assert montecarlo(lambda x:x, MCarlo((1,0.1)),probabilidade=[media-100000*sigma,media+100000*sigma])==1


def test_equivalencia_MCarlo_Medida(): #incertezas pequenas os metodos são equivalentes
   from random import random
   for _ in range(100):
      media1=random()+1;sigma1=(random() +1)*0.01
      media2=random()+1; sigma2=(random()+1)*0.01
      a_carlo= MCarlo((media1,sigma1))
      b_carlo= MCarlo((media2,sigma2))
      a=Medida((media1,sigma1))
      b=Medida((media2,sigma2))
      assert a_carlo+b_carlo==a+b
      assert a_carlo*b_carlo==a*b
      assert a_carlo**b_carlo==a**b
      assert a_carlo/b_carlo==a/b
      assert a_carlo-b_carlo==a-b

def test_exponencias_hiperbolicas():
    import math ; import numpy as np
    for _ in range(100):
      x=MCarlo((10*np.random.random(),1*np.random.random()))
    assert sinh(x)==MCarlo(math.sinh(x.nominal))
    assert cosh(x)==MCarlo(math.cosh(x.nominal))
    assert tanh(x)==MCarlo(math.tanh(x.nominal))
    assert exp(x)==MCarlo(math.exp(x.nominal))
    assert arcsinh(x)==MCarlo(math.asinh(x.nominal))

def test_acosh(): 
   valores_acosh=[(i,math.acosh(i)) for i in range(2,20)]
   for parametro, valor_esperado in valores_acosh:
    assert arccosh(MCarlo((parametro,0.2)))==MCarlo(valor_esperado)

def test_atanh():
   valores_atanh=[(i,math.atanh(i)) for i in np.linspace(-0.9,0.9,100)]
   for parametro, valor_esperado in valores_atanh:
    assert arctanh(MCarlo((parametro,0.02)))==MCarlo(valor_esperado)