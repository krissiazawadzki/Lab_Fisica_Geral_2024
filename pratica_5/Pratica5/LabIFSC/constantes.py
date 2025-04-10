from .medida import Medida
import sys
import inspect 
desnecessarios = [nome for nome, valor in inspect.getmembers(sys.modules[__name__]) if not nome.startswith('__')]

#física
e_charge=Medida((1.602176634e-19,0),"C")
G_gravity=Medida((6.6743015e-11,0),"m^3 kg/s")
h_planck=Medida((6.62607015e-34,0),"J/Hz")
c_speed=Medida((299_792_458,0),"m/s")
epsilon=Medida((8.8541878128e-12,0),"F/m")
mu_mag=Medida((1.25663706219e-6,0),"N/A^2")

#matemática
pi=Medida((3.1415926,0),"")
euler=Medida((2.718281828,0),"")
golden_ratio=Medida((1.6180339,0),"")
nomes_constantes = [nome for nome, valor in inspect.getmembers(sys.modules[__name__]) if not nome.startswith('__') and nome not in desnecessarios]