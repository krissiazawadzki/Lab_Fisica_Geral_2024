from LabIFSC import *
import pytest
from numpy.random import random
import numpy as np
def test_aleatorios():
    nominais=random(10)
    incertezas=random(10)*0.2
    Medidas=np.array([Medida((i,j)) for i,j in zip(nominais,incertezas)])
    MCarlos=np.array([MCarlo((i,j)) for i,j in zip(nominais,incertezas)])
    for elementos in [Medidas,MCarlos]:            
        assert np.array_equal(nominais,getNominal(elementos))
        assert np.array_equal(incertezas,getIncerteza(elementos))

def test_tipos_errados():
  statements=[lambda : getIncerteza([10,5,63,-4,3]),lambda: getIncerteza([1.3,53.1,315.6,-135.]),
              lambda: getIncerteza(["Exemplo de strings","ee","eee"]),
              lambda : getIncerteza(10),lambda : getIncerteza({"hey":313}),lambda: getIncerteza(.13),
              lambda : getNominal([10,5,63,-4,3]),lambda: getNominal([1.3,53.1,315.6,-135.]),
              lambda: getNominal(["Exemplo de strings","ee","eee"]),
              lambda : getNominal(10),lambda : getNominal({"hey":313}),lambda: getNominal(.13)] 
  for index, statement in enumerate(statements):
    with pytest.raises(TypeError):
     statement()
